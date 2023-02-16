##urllib库，Python内置的HTTP请求库
#request : HTTP请求模块
#error : 异常处理模块
#parse : 工具模块， 提供许多URL处理方法， 如拆分、解析、合并
#robotparser ：识别网站的robots.txt文件



# import requests

# url = "https://www.baidu.com/"
# headers = {
#     "user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
# }

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     print(response.text)
# else:
#     print("Failed to access the page with status code:", response.status_code)

import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

print('\n=================================================1=========================================================\n')

#处理异常  URLError
from urllib import request, error
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)
    

print('\n=================================================2=========================================================\n')

##HTTPError
# code: 返回HTTP状态码
# reason: 同父类一样，用于返回错误的原因
# headers: 返回请求头

from urllib import request, error
try:
    response = request.urlopen('https://cuiqingcai.com')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, seq='\n')
    

print('\n=================================================3=========================================================\n')

from urllib import request, error

try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')



print('\n=================================================4=========================================================\n')



import requests
r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.txt))
print(r.txt)
print(r.cookies)


print('\n=================================================5=========================================================\n')


import requests
try:
    r = requests.get('http://httpbin.org/get')
    print(r.text)
except Exception as e:
    print('请求失败')