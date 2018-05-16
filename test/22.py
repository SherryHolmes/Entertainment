# -*- coding:utf-8 -*-
'''
Created on 20160827
@author: qiukang
'''
import requests,time,threading
from bs4 import BeautifulSoup    # HTML

#请求头
headers = {
   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
   'Accept-Encoding':'gzip, deflate, sdch',
   'Accept-Language':'zh-CN,zh;q=0.8',
   'Connection':'keep-alive',
   'Host':'www.zhongchou.com',
   'Upgrade-Insecure-Requests':1,
   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2593.0 Safari/537.36'
}

items = open('pymulti.txt','a')
no = 0
lock = threading.Lock()

# 获得项目url列表
def getItems(urllist):
    # print urllist  #①
    global items,no,lock
    for url in urllist:
        r1 = requests.get(url,headers=headers)
        html = r1.text.encode('utf8')
        soup = BeautifulSoup(html, "lxml");
        lists = soup.findAll(attrs={"class":"ssCardItem"})
        for i in range(len(lists)):
            href = lists[i].a['href']
            lock.acquire()
            items.write(href+"\n")
            no +=1
            # print no
            lock.release()
    
if __name__ == '__main__':
    start = time.clock()
    allpage = 30
    allthread = 30
    per = (int)(allpage/allthread)
    urllist = []
    ths = []
    for page in range(allpage):
        if page==0:
            url = 'http://www.zhongchou.com/browse/di'
        else:
            url = 'http://www.zhongchou.com/browse/di-p'+str(page+1)
        urllist.append(url)
    for i in range(allthread):
        # print urllist[i*(per):(i+1)*(per)]
        th = threading.Thread(target = getItems,args= (urllist[i*(per):(i+1)*(per)],))
        th.start()
        th.join()
    items.close()
    end = time.clock()
    print('it takes %s Seconds to get %s items '%(end-start,no))