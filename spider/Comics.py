# -*- coding: utf-8 -*-
# ------------------------------------------
#   版本：1.0
#   日期：2018-04-01
#   作者：Txz
# ------------------------------------------


from base import Comics
from request import BaseRequest
from urllib import parse
from database import SaveToDatabase
import json
import collections 
import time


class ComicsDm5(Comics):
    """http://www.dm5.com  漫画人"""
    pass


class ComicsKKMH(Comics):
    """https://www.kuaikanmanhua.com 快看漫画"""
    def __init__(self):
        self.lst_kkmh_content = []
        """
        dict[list]
            {
                'href': '',             # 每个章节的地址
                'title': '',            # 每个章节的名字
                'src': '',              # 每个章节的封面地址
                'download_url': [list], # 当前章节的所有内容的地址
            }
        """
        self.keyword = None             # 下载关键字
        self.id = 0                     # 每部漫画保存在数据库中都有唯一的id
        self.save_to_database = None    # 数据库模型


    def _ConnectToDatabase(self):
        """
        连接到数据库
        """
        self.save_to_database = SaveToDatabase("198.13.54.7", "txz", "passwd", "EntertainmentDB", 3306, "utf8")
        self.save_to_database.ConnectDatabase()

    def _CloseDatabase(self):
        """
        关闭数据库
        """
        self.save_to_database.CloseDatabase()

    def _ComicInsert(self, table, sql_dict):
        """插入内容到数据库

        Parameters
        ----------
        table    : str or unicode
                    数据库表名
        sql_dict : dict
                    数据库各字段的字典
            
        Returns
        -------
        success: True
        failed : False
        """

        key     = None
        value   = None
        results = False

        for (k,v) in sql_dict.items(): 
            if key != None:
                key   = "%s,%s"%(key, k)
            else:
                key   = "%s"%(k)

            if value != None:
                value = "%s,%s"%(value, v)
            else:
                value   = "%s"%(v)

        # SQL 插入语句        
        sql = "INSERT INTO %s.%s(%s) VALUES (%s);" %("EntertainmentDB", table, key, value)
        print(sql)
        if self.save_to_database.InsertData(sql):
            results = True
        else:
            print(sql)

        return results


    def _ComicSelect(self, sql):
        """插入内容到数据库

        Parameters
        ----------
        sql    : str or unicode
                 数据库选择语句
            
        Returns
        -------
        success: True
        failed : False
        """
        results = self.save_to_database.SelectData(sql)
        if None == results:
            print(sql)            

        return results


    def _DownloadImg(self, chapter_num, download_path, dct_img_book):
        """下载封面图片和漫画

        Parameters
        ----------
        chapter_num   : int
                        章节号
        download_path : str or unicode
                        存储路径
        dct_img_book : str or unicode
                        需要存储的数据，格式为   
            {
                'href': '',             # 每个章节的地址
                'title': '',            # 每个章节的名字
                'src': '',              # 每个章节的封面地址
                'download_url': [list], # 当前章节的所有内容的地址
            }               
        Returns
        -------
        success: True
        failed : False
        """

        #标题及封面路径
        title         = dct_img_book['title']
        src           = dct_img_book['src']
        download_path = '%s/comics/%s/%s/' %(download_path, self.keyword, title)
        
        #下载封面图片
        count         = 0
        file_name     = 'fengmian.jpg'
        if not BaseRequest.DownloadData(src, download_path, file_name):
            print("download fengmian.jpg failed")
            return False

        #下载漫画内容，图片按1开始自增
        for url in dct_img_book['download_url']:
            count += 1
            file_name = '%d.jgp' %(count)
            for i in range(5):
                if not BaseRequest.DownloadData(url, download_path, file_name):
                    print("download %s failed %d time" % (file_name, i))
                else:
                    break

        #将章节信息保存到章节表中
        sql_dict = collections.OrderedDict()
        sql_dict['ChapterNum']   = chapter_num          #章节号
        sql_dict['ChapterName']  = "\"" + title + "\""  #章节名称
        sql_dict['PicNum']       = count                #图片数量
        sql_dict['Dept_ID']      = self.id              #外键，关联漫画名称表，与其id相同
        
        #插入数据到章节表中
        if not self._ComicInsert('ComicChapter', sql_dict):
            print("inster ComicChapter table failed!")
        
        return True



    def _GetContentByKeyword(self, keyword):
        """通过关键字查找到需要的内容，然后将返回的内容记录在kkmh_content结构中

        Parameters
        ----------
        keyword : str or unicode
            搜索文字
        Returns
        -------
        success: dict[list]--self.kkmh_content
        failed : None
        """

        #请求keyword网页
        self.keyword       = keyword
        url_keyword        = self._url + '/web/topic/search?keyword' +  parse.urlencode({"": keyword})
        content_keyword    = BaseRequest.GetUrlContent(url_keyword)
        if content_keyword == False:
            return None

        #将返回的内容解析
        content_keyword_json = json.loads(content_keyword.decode("utf8"))
        if content_keyword_json == False:
            return None

        #取出id关键字，从而访问搜索到的内容
        url_keyword_content = self._url + '/web/topic/' + str(content_keyword_json['data']['topic'][0]['id'])
        soup_keyword_content = BaseRequest.GetUrlSoup(url_keyword_content)
        if soup_keyword_content == False:
            return None

        #将漫画信息存储到数据库
        sql_dict = collections.OrderedDict()
        sql_dict['Name']    = "\"" + self.keyword + "\""      #名字
        sql_dict['Num']     = 0                               #编号  
        sql_dict['Website'] = "\"" + self._url + "\""         #网址
        sql_dict['Time']    = "\"" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\"" #下载时间
        if not self._ComicInsert('ComicName', sql_dict):
            print("inster ComicName table failed!")

        #获取漫画编号，唯一
        sql = "SELECT ID FROM EntertainmentDB.ComicName WHERE Name=\"%s\";" %(self.keyword)
        max_id = self._ComicSelect(sql)
        self.id = max_id[0][0]

        #找到漫画所有章节的地址,由于网页的顺序是从最后一章至第一章，所以要反向循环
        a_book = soup_keyword_content.find_all('a',{'class':'article-img'})
        for book in reversed(a_book):
            href  = book['href']
            title = book['title']
            src   = book.img['src']
            lst_img_book = []
            dct_img_book = {}

            #下载当前章节的内容
            url_a_book  = self._url + href
            soup_a_book = BaseRequest.GetUrlSoup(url_a_book)
            if soup_a_book == None:
                return None

            #找到每一章节的图片地址并保存
            content_img_book = soup_a_book.find_all('img',{'class':'kklazy', 'title':title})
            for img_book in content_img_book:
                lst_img_book.append(img_book['data-kksrc'].replace('amp;', ''))

            #将数据存储到结构体中,用于后续保存
            dct_img_book = {'href':href, 'title':title, 'src':src, 'download_url':lst_img_book}
            self.lst_kkmh_content.append(dct_img_book)

            yield dct_img_book

        


        