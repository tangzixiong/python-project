##txt文本存储
import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
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
""" with open('explore.txt', 'a', encoding='utf-8') as file:            ##如保存时将原文清空，可将第二个参数改写为 w   ##a: 以追加方式打开一个文件
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n') """
    
    
##读取JSON
import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
},{
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print((type(str)))
data = json.loads(str)
print(data)
print(type(data))

##输出Json
import json

data = [{
    'name' :'Bob',
    'gender' : 'female',
    'birthday': '1992-10-18'
}]

with open('data.json', 'w') as file:
    file.write(json.dumps(data))