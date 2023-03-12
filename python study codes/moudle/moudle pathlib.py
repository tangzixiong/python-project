## pathlib 模块

# http://www.ityouknow.com/python/2019/10/19/python-pathlib-035.html


## pathlib 模块提供了表示文件系统路径的类，可适用于不同的操作系统。
# 使用 pathlib 模块，相比于 os 模块可以写出更简洁，易读的代码。
# pathlib 模块中的 Path 类继承自 PurePath，对 PurePath 中的部分
# 方法进行了重载，相比于 os.path 有更高的抽象级别


##获取目录
# Path.cwd()  返回文件当前所在目录
# Path.home() 返回用户的主目录

from pathlib import Path

currentPath = Path.cwd()
homePath = Path.home()
print("文件当前所在目录：%s\n用户主目录:%s" %(currentPath, homePath))


##目录拼接

#斜杠/操作符用于拼接路径

from pathlib import Path
currentPath = Path.cwd()
newPath = currentPath / 'py-100'
print("新目录为：%s" %(newPath))


##创建、删除目录

#Path.mkdir(), 创建给定路径的目录
#Path.rmdir(), 删除该目录，目录文件夹必须为空

from pathlib import Path
currentPath = Path.cwd()
makePath = currentPath / 'python-1000'
makePath.mkdir()
print("创建的目录为：%s" %(makePath))