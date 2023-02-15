""" #-*-coding:gb2312 -*-

# 模块定义为一个函数库，包含两个函数供其他函数使用，
# yanghui(n)用于输出n阶杨辉三角,
# hannuota(n)用于完成n层hannuota(n) 移动模拟


##########杨辉三角函数yanghui(n)##########
# def yanghui(n):
#     if not str(n).isdecimal() or n<2 or n>25:
#         #限制阶数，避免数字过大
#         print('yanghui(n), 参数n必须是不小于2且不大于25的正整数')
#         return False
#         #使用列表对象生成杨辉三角
#         x=[]
#         for i in range(1,n+1):
#             x.append([1]*i)
#         #计算杨辉三角矩阵其他值
#         for i in range(2,n):
#             for j in range(1,i):
#                 x[i][j]=x[i-1][j-1]+x[i-1][j]
#         #输出杨辉三角
#         for i in range(n):
#             if n<=10:print(' '*(40-4*i),end='')
#             for j in range(i+1):
#                 print('%-8d'%x[i][j],end='')
#             print()

# if __name__=='__mian__':
#     print('模块独立自运行测试输出：')
#     print('一、10阶杨辉三角如下:')
#     yanghui(10)  """

###################################################################


# row = int(input("请输入你想要的三角形层数："))
 
# A = [0,1,0]
 
# for i in range(row):
   
#     A = [A[j]+A[j+1] for j in range(i+1)]
    
#     print(*A)           #将A的内容逐一打印出来
 
#     A.insert(0,0)
#     A.append(0)

####################################################################

n = eval(input("请问你想生成几层的杨辉三角呢？"))
result= []

def fun(N):   # 杨辉三角生成函数
    if N == 1:
        result.append([1])
    elif N == 2:
        result.append([1])
        result.append([1,1])
    else:
        result.append([1])
        result.append([1,1])
        for i in range(3, N+1):
            temps = []             # 用来存放第i行的所有数
            temps.append(1)        # 每行第一个数是1
            for j in range(i-2):   # 生成第i行第2个数 到 倒数第2个数
                temp = result[i-2][j] + result[i-2][j+1]
                temps.append(temp)
            temps.append(1)        # 每行倒数第一个数是1
            result.append(temps)   # 将第i行的所有数添加到列表

    return result

# triangles = fun(n)
# for line in triangles:
#     print(line)

triangles = fun(n)
for line in range(len(triangles)):
    for x in range(len(triangles[line])):
        triangles[line][x] = str(triangles[line][x])
    triangles[line] = '   '.join(triangles[line])
    print("第{:>2}行   {:^100}".format(line+1, triangles[line]))
