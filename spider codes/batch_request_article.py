
#批量爬取下载小说至txt文本

#原文链接：https://blog.csdn.net/weixin_54852327/article/details/115916146

import requests
from bs4 import BeautifulSoup

def geturl():
    url = "https://www.xqb5200.com/95_95204/"
    header = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
    req = requests.get(url = url, headers = header)
    req.encoding = 'gbk'
    html = req.text
    bes = BeautifulSoup(html, "lxml")
    
    texts = bes.find('div', id='list')
    chapters = texts.find_all('a')              #该函数可以返回list下的标签为a的所有信息
    words = []                                  #创建空的列表，存入每章节的url与章节名称
    ##对标签a的内容进行提取
    for chapter in chapters:
        name = chapter.string                   #取出字符串,可以看出字符串只有章节号与章节名称，刚好符合我们所需
        url1 = url + chapter.get('href')        #获得每一章节的url，可从html代码中看到每一个"href"前边均缺少初始的url，因此需要加上
        word = [url1, name]                     #以列表格式存储
        words.append(word)                      #最终加入总的大列表中并返回
    return words

if __name__ == '__main__':
    target = geturl()
    header = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
    
    for tar in target:
        req = requests.get(url=tar[0], headers = header)
        req.encoding = 'gbk'
        html = req.text
        bes = BeautifulSoup(html, 'lxml')
        texts = bes.find('div', id = 'content')
        texts_list = texts.text.split('\xa0')
        with open('./spider codes/novels/'+ tar[1] + ".txt", "w") as file:
            for line in texts_list:
                file.write(line+"\n")