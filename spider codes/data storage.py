##txt文本存储
import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()
    
    


##文件写入简写方法，使用with...as... 语法
with open('explore.txt', 'a', encoding='utf-8') as file:            ##如保存时将原文清空，可将第二个参数改写为 w   ##a: 以追加方式打开一个文件
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')