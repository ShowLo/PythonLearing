import requests
import re

def getHtmlText(url):
    """
    获取网页信息的函数
    the function to get information form the web page
    :param url: string -- url link,url链接
    :return: string -- information of the web page,网页信息
    """
    try:
        kv = {'user-agent':'Mozila/5.0'};                                           #模仿浏览器行为
        r = requests.get(url,timeout = 30,headers = kv);
        r.raise_for_status();
        if r.encoding == 'ISO-8859-1':
            r.encoding = r.apparent_encoding;
        return r.text;
    except:
        print('exception occured in getHtmlText()');

def getInfoFromTaobao(keyWords,num):
    """
    根据搜索关键词，从淘宝获取相应的搜索页面信息
    According to search keyterms, get the corresponding information of the search page from Taobao
    :param keyWords:list -- keywords to search,搜索的关键词
    :param num:int -- number of web pages,搜索页面的数量
    :return:string -- the imformation of the webpage,网页信息
    """
    try:
        url = 'https://s.taobao.com/search?q=';
        wordsNum = len(keyWords);
        for i in range(wordsNum - 1):
            url += keyWords[i] + '+';
        url += keyWords[wordsNum - 1] + '&s=';
        for i in range(num):
            ithPageUrl = url + str(44 * i);
            info = getHtmlText(ithPageUrl);
            