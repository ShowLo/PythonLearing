import requests
from bs4 import BeautifulSoup
import bs4
import xlwt
import os

#获取网页信息的函数
def getHTMLText(url):
    """
    :param url: string
    :return: string
    """
    try:
        kv = {'user-agent':'Mozila/5.0'};                                           #模仿浏览器行为
        r = requests.get(url,timeout = 30,headers = kv);
        r.raise_for_status();
        if r.encoding == 'ISO-8859-1':
            r.encoding = r.apparent_encoding;                                       #改为正确的编码
        return r.text;
    except:
        return ''

#将爬取到的大学排名信息保存于list中
def fillUniversityList(ulist,html):
    """
    :param ulist: list
    :param html: string
    """
    soup = BeautifulSoup(html,'lxml');
    for tr in soup.find('tbody').children:                                          #找到放置排名信息的地方
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td');
            ulist.append([tds[0].string,tds[1].string,tds[3].string]);              #加入排名、学习名称和总分信息

#打印函数
def printUlist(ulist,num):
    print('{:^10}\t{:^10}\t{:^10}'.format('排名','学校名称','总分'))
    for i in range(num):
        u = ulist[i];
        print('{:^10}\t{:^10}\t{:^10}'.format(u[0],u[1],u[2]));

#保存为excel文件
def savaAsExcel(ulist,num,filePath,fileName):
    """
    :param ulist: list
    :param num: int
    :param filePath: string
    :param fileName: string
    """
    workbook = xlwt.Workbook(encoding='ascii');                                     #创建Excel工作表
    worksheet = workbook.add_sheet('universityRanking');
    colNum = len(ulist[0]);

    completePath = filePath + '/' + fileName;                                       #完整路径
    if not os.path.exists(filePath):                                                #判断路径是否存在，不存在的话创建之
        os.makedirs(filePath);
    if os.path.exists(completePath):                                                #文件已经存在，删除掉
        os.remove(completePath);

    worksheet.write(0,0,'排名');                                                    #写入表头信息
    worksheet.write(0,1,'学校名称');
    worksheet.write(0,2,'总分');
    for i in range(num):                                                            #写入详细信息
        for j in range(colNum):
            worksheet.write(i+1,j,ulist[i][j]);

    workbook.save(completePath);                                                    #保存文件


def main():
    uinfo = [];
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html';
    html = getHTMLText(url);
    fillUniversityList(uinfo,html);
    filePath = 'D://爬虫获取//excel/';
    fileName = 'universityRanking.xls';
    savaAsExcel(uinfo,100,filePath,fileName);
    
main();