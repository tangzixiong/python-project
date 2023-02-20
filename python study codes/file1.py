
## 写入文件
# write(): 能够将传入的字符串写入文件(覆盖)， 并返回写入的字符长度
# writelines(): 能够将一个序列的字符串写入文件， 如换行要手动添加换行符\n

f = open('test1.txt', 'w', encoding='utf-8')
str = 'Python'
n = f.write(str)                                   #写入字符
print(n)                                           #显示写入字符长度
f.close()



##使用writelines()方法将字符串列表写入打开的test1.txt文件

f = open('test1.txt', 'a+', encoding='utf-8')
list = ['python', 'java', 'c']
f.writelines(list)
list = ['\npython', '\njava', '\nc' ]
f.writelines(list)
f.close()

