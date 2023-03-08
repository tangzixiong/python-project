
##zipfil模块
#zipfile模块用来做zip格式编码的压缩和解压缩
import zipfile


## zipfile.ZipFile(path, 'mode')

# file为文件的路径
# mode可以取r、w、a。
# r表示只读，w表示重写，a表示添加。
# 功能：创建一个zip文件对象，并根据mode选择打开方式。



## zip.extract(name, path, pwd)

# name表示文件名
# path表解压到的目的路径，默认为压缩包所在的路径
# pwd为解压密码
# 功能：将压缩包解压，并将解压文件存放在目的路径中。

""" 
import zipfile
zip_file = zipfile.ZipFile(path, 'r')
for names in zip_file.namelist():
    zip_file.extract(names, path) 
"""
