#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-

#from urllib.request import urlopen
#from bs4 import BeautifulSoup
#html = urlopen("http://www.pythonscraping.com/pages/page1.html")
#html = urlopen("http://www.epri.sgcc.com.cn/html/epri/col1010000066/column_1010000066_1.html")
#print(html.read())
#bsObj = BeautifulSoup(html.read())
#print(bsObj.h1)

# -*- coding: utf-8 -*-

# 引入模块
import os
import re 
import urllib
from bs4 import BeautifulSoup

#创建目录
def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
 
        print(path+'创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+'目录已存在')
        return False 


#获取网页的所有标签
def get_html_res(url):
    try:
        res = urllib.request.urlopen(url)
    except Exception as e:
        print(e)
        return None 
    else:
        if res is None:
            print('没有找到网页')
            return None

    try:
        soup = BeautifulSoup(res,"html.parser")
    except AttributeError as e:
        print("BeautifulSoup parser failed!")
        return None 

    return soup


#下载文档
def download_doc(url):
    # 获取url的全部标签
    soup = get_html_res(url)
    if soup == 'False':
        return False

    #找到所有objid=6055的行
    a_book = soup.find_all('a',{'objid':'6055'})
    for book in a_book:

        #获取文件名字
        name = book.get_text()
        # 去除首位空格
        name = name.strip()
        name = name.replace("\n", "")

        #获取文件日期
        dict = book.attrs
        if 'href' in dict.keys():
            str_href = dict['href'].split('/')
            if len(str_href) > 5:
                time = str_href[4] + "-" + str_href[5]
            else:
                time = "2000-1-1"

        #创建下载保存的路径
        download_path = '/home/txz/test/download/%s/%s' %(time,name)
        mkdir_result = mkdir(download_path)


        if mkdir_result == True:

                #上面网页中的所有要下载的文档的主路径,并下载其内容
                url_child = "http://www.epri.sgcc.com.cn"+dict['href']
                print(url_child)
                try:
                        urllib.request.urlretrieve(url_child,r'%s/content.doc'%download_path)
                except Exception as e:
                        print(e)

                #找到子网页内的所有doc pdf 等文档
                soup_child = get_html_res(url_child)
                if soup_child is None:
                    continue

                    #找所允许下载的文档
                download_book = soup_child.find_all(href=re.compile('\.doc$|\.pdf$|\.rar$|\.xls$'))
                for book_child in download_book:
                    #获取文件名字
                    name_child = book_child.get_text()

                    #如果文件名字为空，随便起个名字
                    if len(name_child) <= 0:
                        name_child = "1.doc"

                    #如果有下载路径则开始下载
                    dict_child = book_child.attrs
                    if 'href' in dict_child.keys(): 
                        #下载所需文档
                        download_url="http://www.epri.sgcc.com.cn"+dict_child['href']
                        filename = '%s/%s' %(download_path,name_child)

                        try:
                            urllib.request.urlretrieve(download_url,r'%s'%filename)
                        except Exception as e:
                            print(e)
        else:
            print("此路径已经下载过,忽略其内容！")  


if __name__ == "__main__":
    print ("开始下载文档...")
    url = "http://www.epri.sgcc.com.cn/html/epri/col1010000066/column_1010000066_1.html"
    print ("下载路径为：%s" %url)
    result = download_doc(url)
    if result == 'False':
        print ("下载失败...")
    else:
        print ("%s下载完成" %(url))
    print("\n\n\n\n")
    url = "http://www.epri.sgcc.com.cn/html/epri/col1230000189/column_1230000189_1.html"
    print ("下载路径为：%s" %url)
    result = download_doc(url)
    if result == 'False':
        print ("下载失败...")
    else:
        print ("%s下载完成" %(url))
