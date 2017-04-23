﻿# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozila/5.0'};                                           #模仿浏览器行为
        r = requests.get(url,timeout = 30,headers = kv);
        r.raise_for_status();
        if r.encoding == 'ISO-8859-1':
            r.encoding = r.apparent_encoding;                                       #改为正确的编码
        return r.text;
    except:
        return ''

def fillUniversityList(ulist,html):
    soup = BeautifulSoup(html,'lxml');
    for tr in soup.find('tbody').children:                                          #找到放置排名信息的地方
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td');
            ulist.append([tds[0].string,tds[1].string,tds[3].string]);              #加入排名、学习名称和总分信息
    
def printUlist(ulist,num):
    print('{:^10}\t{:^10}\t{:^10}'.format('排名','学校名称','总分'))
    for i in range(num):
        u = ulist[i];
        print('{:^10}\t{:^10}\t{:^10}'.format(u[0],u[1],u[2]));
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html';
    html = getHTMLText(url);
    fillUniversityList(uinfo,html);
    printUlist(uinfo,20)
    
main();