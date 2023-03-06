
##网页批量爬取文本

import requests
#from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://www.xqb5200.com/95_95204/49370156.html' #目标访问网站url
    #伪装头信息的引入
    header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    req = requests.get(url=url, headers=header)             #返回爬取网站信息
    req.encoding = 'gbk'                                    #查看head中charset可以查找到编码信息
    html = req.text                                         #转化为文本
    #print(html)
   
# f = open('novel.txt', 'w', encoding='gbk')
# n = f.write(html)
# print(n)
# f.close()



#BeautifulSoup库的解析数据功能,BeautifulSoup库是BeautifulSoup4库（一般书写为bs4）中的子库。
""" 
import bs4 from BeautifulSoup
#html接上文中的已爬取得到的全部信息
bes= BeautifulSoup(html,"lxml")#通过lxml方式解析获取网页中文本信息
#解析text中，提取标签为"div"内id = "content"全部信息，也可解析提取class = <某名称>的内容信息 
text = bes.find("div", id = "content"[,class_ = "<class的名称>"]) 
"""

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://www.xqb5200.com/95_95204/49370156.html'
    header = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
    req = requests.get(url=url, headers=header)
    req.encoding = 'gbk'                                    #查看head中charset可以查找到编码信息
    html = req.text 
    bes = BeautifulSoup(html,'lxml')                        #通过lxml方式解析获取网页中文本信息
    texts = bes.find('div', id = 'content')
    #print(texts)
    
    texts_list = texts.text.split("\xa0"*4)                 #消除每段的开头处存在四个空格键
    #print(texts_list)
    with open('novel.txt', 'w') as file:
        for line in texts_list:
            file.write(line+"\n")