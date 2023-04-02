import torch

x = torch.arange(12)
print(x) 


##张量表示一个由数值组成的数组，这个数组可能有多个维度。 具有一个轴的张量对应数学上的向量（vector）； 
# 具有两个轴的张量对应数学上的矩阵（matrix）； 具有两个轴以上的张量没有特殊的数学名称

print(x.shape)      #torch.Size([12]) 可以通过张量的shape属性来访问张量（沿每个轴的长度）的形状

print(x.numel())

#要想改变一个张量的形状而不改变元素数量和元素值，可以调用reshape函数
print(x.reshape(3, 4))

#们可以通过-1来调用此自动计算出维度的功能

print(x.reshape(-1,4))
print(x.reshape(3,-1))

print(torch.zeros((2,3,4)))     #创建一个形状为(2,3,4)的张量，其中所有元素都设置为0

print(torch.ones((2,3,4)))      #创建一个形状为(2,3,4)的张量，其中所有元素都设置为1


#创建一个形状为（3,4）的张量。 其中的每个元素都从均值为0、标准差为1的标准高斯分布（正态分布）中随机采样。
print(torch.randn(3, 4))


print(torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]]))

