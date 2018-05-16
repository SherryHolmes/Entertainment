# -*- coding: utf-8 -*-

from Comics import ComicsKKMH

cComicsKKMH = ComicsKKMH()

class EntertainmentAPI(object):
    """外部接口"""
    def __init__(self):
        pass

    def LogIn(self, user, passward):
        return cComicsKKMH._LogIn()

    def SetLoginInfo(self, url, username=None, password=None):  
        return cComicsKKMH._set_info(url, username, password)

    def GetContentByKeyword(self, download_path, keyword):
        results = True
        chapter_num = 1
        cComicsKKMH._ConnectToDatabase()
        for dct_img_book in cComicsKKMH._GetContentByKeyword(keyword):
            if not cComicsKKMH._DownloadImg(chapter_num, download_path, dct_img_book):
                print("download %s failed" %dct_img_book)
                results = False
            chapter_num = chapter_num + 1

        cComicsKKMH._CloseDatabase()
        return results

    def ParseContent(self, content):
        return cComicsKKMH._ParseContent(content)

    def DownloadImg(self, download_path, dct_img_book):
        return cComicsKKMH._DownloadImg(download_path, dct_img_book)


EntertainmentAPi = EntertainmentAPI()
EntertainmentAPi.SetLoginInfo("https://www.kuaikanmanhua.com")
if not EntertainmentAPi.GetContentByKeyword("/home/txz/download","海贼王"):
    print("download failed!")

#if not EntertainmentAPi.SaveToDatabase('/home/txz/download',dct_img_book):
#    print("download failed!")
#EntertainmentAPi.ParseContent(content)
