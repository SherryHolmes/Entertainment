# -*- coding: utf-8 -*-

class EntertainmentSpider(object):
    """娱乐基类"""
    def __init__(self):
        self._user     = None        # 用户名
        self._passward = None        # 密码
        self._url      = None        # 网址

    def _log_in(self):
        pass        

    def _set_info(self, url, username=None, password=None):
        self._user     = username        # 用户名
        self._passward = password        # 密码
        self._url      = url             # 网址


class Comics(EntertainmentSpider):
    """漫画类,所有漫画网站的基类"""
    pass