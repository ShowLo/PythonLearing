import requests
import os

def savePhoto(url):
    filepath = 'D://爬虫获取//图片/';
    path = filepath + url.split('/')[-1];
    try:
        if not os.path.exists(filepath):                    #判断路径是否存在，不存在的话创建之
            os.makedirs(filepath);
        if not os.path.exists(path):                        #判断图片是否存在，不存在的话才访问并保存
            kv = {'user-agent': 'Mozila/5.0'};              #模仿浏览器
            r = requests.get(url,timeout = 30,headers = kv);
            with open(path,'wb') as f:
                f.write(r.content);                         #以二进制方式保存图片
                f.close();
                #print('save!');
        else:
            print('The photo already exists!');
    except:
        print('exception occurs!');

if __name__ == 'main':
    url = 'http://wx3.sinaimg.cn/mw690/71b2cbb3ly1fehwbrppacj21kw2i6k2r.jpg';
    savePhoto(url);