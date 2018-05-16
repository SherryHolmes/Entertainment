# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, print_function
from  urllib import request,parse
from bs4 import BeautifulSoup
import copy
import random
import os

def AddAgent():
    # User-Agent 列表
    useragent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3"
    ]
    # 随机选择一个User-Agent字符串
    # random.choice()这个方法可以从列表中随机的取出一个元素
    return random.choice(useragent_list)

def Mkdir(path):
    """创建目录

    Parameters
    ----------
    path : str or unicode
           路径
    Returns
    -------
    success: True 
    failed : False
    """
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



class BaseRequest(object):

    @staticmethod
    def GetUrlContent(url):
        """获取当前网页的内容

        Parameters
        ----------
        url : str or unicode
              需要下载的地址
        Returns
        -------
        success: str 
                 当前网页的内容
        failed : None
        """
        user_agent = AddAgent()
        try:
            # 构造请求对象
            req = request.Request(url)
            # 添加一个请求报头,添加的时候是User-Agent
            req.add_header("User-Agent", user_agent)

            # 发送请求，返回服务器响应
            reseponse = request.urlopen(req)
        except Exception as e:
            print(e)
            return None 
        else:
            if reseponse is None:
                print('没有找到网页')
                return None

        # 返回响应的html内容
        return reseponse.read()


    @staticmethod
    def GetUrlSoup(url):
        """获取当前网页beautifulsoup解析后的内容

        Parameters
        ----------
        url : str or unicode
              需要下载的地址
        Returns
        -------
        success: bs4 
                 当前网页的内容
        failed : None
        """
        user_agent = AddAgent()
        try:
            # 构造请求对象
            req = request.Request(url)
            # 添加一个请求报头,添加的时候是User-Agent
            req.add_header("User-Agent", user_agent)

            # 发送请求，返回服务器响应
            reseponse = request.urlopen(req)
        except Exception as e:
            print(e)
            return None 
        else:
            if reseponse is None:
                print('没有找到网页')
                return None


        try:
            #BeautifulSoup解析网页
            soup = BeautifulSoup(reseponse,"html.parser")
        except AttributeError as e:
            print("BeautifulSoup parser failed!")
            return None 

        # 返回解析后的网页内容
        return soup

    @staticmethod
    def DownloadData(download_url, download_path, file_name):
        """下载数据

        Parameters
        ----------
        download_url : str or unicode
                       需要下载的地址
        download_path：str or unicode
                       需要存储的路径
        Returns
        -------
        success: True 
        failed : False
        """

        if not os.path.exists(download_path):
            if not Mkdir(download_path):
                print("path is exists")

        path = download_path + file_name
        if os.path.isfile(path):
            print("%s is exists"%path)
            return True

        try:
            request.urlretrieve(download_url, path)
        except Exception as e:
            print(e)
            return False

        return True