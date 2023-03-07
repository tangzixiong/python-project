
#!/usr/bin/python3
# 文件名: using_sys.py

import sys

print('命令行参数如下:')
for i in sys.argv:          #sys.argv 是一个包含命令行参数的列表
   print(i)

print('\n\nPython 路径为：', sys.path, '\n')      #sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表