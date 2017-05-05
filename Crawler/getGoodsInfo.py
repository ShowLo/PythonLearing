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
        kv = {'user-agent': 'Mozila/5.0'};                                           #模仿浏览器行为
        r = requests.get(url, timeout=30, headers=kv);
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

        #根据关键词构建搜索页面网址
        for i in range(wordsNum - 1):
            url += keyWords[i] + '+';
        url += keyWords[wordsNum - 1] + '&s=';
        infoList = [];
        for i in range(num):
            #构建第i+1页的网址
            ithPageUrl = url + str(44 * i);
            htmlText = getHtmlText(ithPageUrl);
            #分别获取商品名称、价格及付款数信息
            name = re.findall(r'"raw_title":".*?"', htmlText);
            price = re.findall(r'"view_price":"\d+\.*\d*"', htmlText);
            saleNum = re.findall(r'"view_sales":"\d+人付款"', htmlText);
            for i in range(len(name)):
                ithName = name[i].split(':')[1][1:-1];
                ithPrice = eval(price[i].split(':')[1][1:-1]);
                ithSaleNum = eval(saleNum[i].split(':')[1][1:-4]);
                infoList.append([ithName,ithPrice,ithSaleNum]);
        return infoList;
    except:
        print('exception occured in getInfoFromTaobao()');

def printInfo(infoList):
    """
    打印从淘宝获取的商品信息
    print the goods information gotten form Taobao
    :param infoList:list,the list of information,存储商品信息的list
    """
    num = len(infoList);
    style = '{:20}\t{:10}\t{:10}';
    print(style.format('商品名称', '商品价格', '付款人数'))
    for i in range(num):
        ithGoodsInfo = infoList[i];
        print(style.format(ithGoodsInfo[0], ithGoodsInfo[1], ithGoodsInfo[2]));

def main():
    keyWords = ['裤子', '男', '夏'];
    num = 3;
    infoList = getInfoFromTaobao(keyWords,num);
    printInfo(infoList);

main();