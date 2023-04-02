#线性代数

# https://zh-v2.d2l.ai/chapter_preliminaries/linear-algebra.html

## 标量(scalar)

import torch

x = torch.tensor(3.0)
y = torch.tensor(2.0)

#print(x+y, x*y, x/y, x**y, sep='\n') 

""" 
tensor(5.)
tensor(6.)
tensor(1.5000)
tensor(9.)
"""


##向量(vector)

x = torch.arange(4)
#print(x)


""" 
tensor([0, 1, 2, 3])
"""
print(x[3])


## 矩阵

A = torch.arange(20).reshape(5, 4)
print(A)

print(A.T)      #矩阵的转置

B = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
print(B)

print(B == B.T)


## 张量

X = torch.arange(24).reshape(2, 3, 4)
print(X)

## 张量算法的基本性质

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = A.clone()       #通过分配新内存，将A的一个副本分配给B
print(A, A+B, sep='\n')

print(A*B)          #两个矩阵的按元素乘法称为Hadamard积

#将张量乘以或加上一个标量不会改变张量的形状，其中张量的每个元素都将与标量相加或相乘

a = 2
X = torch.arange(24).reshape(2, 3, 4)
print(a+X, (a * X).shape)

## 点积
x = torch.arange(4, dtype = torch.float32)
y = torch.ones(4, dtype = torch.float32)
print(x, y, torch.dot(x, y))

print(torch.sum(x * y))     #我们可以通过执行按元素乘法，然后进行求和来表示两个向量的点积


## 矩阵-向量积

# 使用张量表示矩阵-向量积，我们使用mv函数。 
# 当我们为矩阵A和向量x调用torch.mv(A, x)时，会执行矩阵-向量积

print(A.shape, x.shape, torch.mv(A, x))



##矩阵-矩阵乘法

B = torch.ones(4, 3)
print(torch.mm(A, B))

## 范数

u = torch.tensor([3.0, -4.0])
print(torch.norm(u))        #计算L_2范数

print(torch.abs(u).sum())   #计算L_1范数

print(torch.norm(torch.ones((4,9))))      #计算矩阵的Frobenius范数