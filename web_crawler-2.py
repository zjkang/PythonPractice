#!/usr/bin/env python
# coding=utf-8
# 这段代码是用来下载“中医世家”网站上的书籍的，很不好意思了！
import chardet
import urllib2,urllib,os
import sys
from bs4 import BeautifulSoup

#定义书籍链接列表
mainbooklink = ["http://www.zysj.com.cn/lilunshuji/1index.html"]
        # "http://www.zysj.com.cn/lilunshuji/5index.html",
        # "http://www.zysj.com.cn/lilunshuji/20index.html",
        # "http://www.zysj.com.cn/lilunshuji/25index.html"]

bookdir = [u"d://book//中医教材//",u"d://book//中医著作//",u"d://book//实用手册//",
            u"d://book//西医备考//"]
chmname = [] #chm电子书中文名字
chmbooklink = [] #对应chm的下载地址
#该函数实现获取一个地址后马上下载该书籍


def getbooklink(url):
    #检测url地址——暂时略了！
    
    #获取url地址的网页,并使用BeautifulSoup进行解析
    req = urllib2.Request(
            url = url,
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4'}
        )
    
    content = urllib2.urlopen(req).read()

    typeEncode = sys.getfilesystemencoding()##系统默认编码
    infoencode = chardet.detect(content).get('encoding','utf-8')##通过第3方模块来自动提取网页的编码
    html = content.decode(infoencode,'ignore').encode(typeEncode)##先转换成unicode编码，然后转换系统编码输出
    # print html

    soup = BeautifulSoup(html)
 
    #处理url，取得其前部地址，用以确定下面得到的地址的完全地址
    urllen = len(url)
    
    
    for i in soup('li'):

        print i.a.attrs
        # print i.a['title'].decode('utf8').encode('utf8')
        # print i.a['title'].decode('utf8').encode('utf8')
        # print i.a.content
        print i.a.string.encode('utf8')
        # i.a['href']
        # chmfilename = i.a.string
        # print chmfilename
    #     bookfilelink = "http://www.zysj.com.cn"+i.a['href']
        
    #     page = urllib2.urlopen(bookfilelink)
    #     soup =BeautifulSoup(page)
    #     ti = u"下载电子书："+chmfilename+".chm"
        # for k in soup('a',title = ti):
        #     chmname.append(chmfilename+'.chm')
        #     downlink = "http://www.zysj.com.cn"+k['href']
        #     chmbooklink.append(downlink)
        #     print chmfilename.encode('gb2312')+'.chm',downlink

            
# def downbook(filename,url,dirn):
#     #urllib.urlretrieve(url, filename)
#     if not os.path.exists(bookdir(dirn)):
#         os.makedirs(bookdir(dirn))
        
#     print "开始下载：".decode('utf-8').encode('gb2312'),filename.encode('gb2312')
#     filename = bookdir[dirn]+filename
#     urllib.urlretrieve(url,filename)
#     print "下载完成！".decode('utf-8').encode('gb2312')

if __name__=="__main__":
    dirn = 0
    typeEncode = sys.getfilesystemencoding()##系统默认编码

    print typeEncode

    for i in mainbooklink:
        print i
        getbooklink(i)
        # for j in range(0,len(chmname)):
        #     downbook(chmname[j],chmbooklink[j],dirn)
        chmname = []
        chmbooklink = []
        dirn = dirn+1
    
    
    
"""
这一小段代码是用来学习查找字符串里面出现的某个字符的呃位置，我把所有的位置都取出来了，接下来想怎样就能怎样了！
a ="http://www.zysj.com.cn/lilunshuji/1index.html"
b = 0
c = len(a)
while 1:
    b = a.find('/',b,c)
    print b
    b = b + 1
    if b == 0:
        break
"""