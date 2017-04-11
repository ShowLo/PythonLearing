import requests
import re
def searchIP(IP):
    try:
        url = 'http://www.ip138.com/ips138.asp?ip=' + IP;                           #用来查询IP地址的url
        kv = {'user-agent':'Mozila/5.0'};                                           #模仿浏览器行为
        r = requests.get(url,timeout = 30,headers = kv);
        r.raise_for_status();
        if r.encoding == 'ISO-8859-1':
            r.encoding = r.apparent_encoding;

        address = re.search('<li>本站数据：(?P<realAddress>.+?)</li>',r.text);      #找到存放IP地址的数据所在
        address1 = re.search('<li>参考数据1：(?P<realAddress1>.+?)</li>',r.text);   #找到参考地址1
        address2 = re.search('<li>参考数据2：(?P<realAddress2>.+?)</li>',r.text);   #找到参考地址2

        addressList = [];
        addressList.append(address.group('realAddress'));
        addressList.append(address1.group('realAddress1'));
        addressList.append(address2.group('realAddress2'));
        return addressList;
    except:
        print('exception!');

IP = '59.66.141.44';
print(searchIP(IP));