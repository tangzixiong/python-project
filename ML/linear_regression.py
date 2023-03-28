
import torch
#数据作为矩阵参与Tensor

x_data = torch.Tensor([[1.0], [2.0], [3.0]])                        ## 准备数据集                        
y_data = torch.Tensor([[2.0], [4.0], [6.0]])

#固定继承于Module
class LinearModel(torch.nn.Module):
    #构造函数初始化
    def __init__(self):
        #调用父类的init
        super(LinearModel, self).__init__()
        #Linear对象包括weight(w)以及bias(b)两个成员张量
        self.linear = torch.nn.Linear(1, 1)
    
    #前馈函数forward, 对父类函数中的overwrite
    def forward(self, x):
        #调用linear中的call(), 以利用父类forward()计算wx+b
        y_pred = self.linear(x)
        return y_pred
    #反馈函数backward由module自动根据计算图生成
    
model = LinearModel()                                               ##设计模型

#构造的criterion对象所接受的参数为(y', y)
criterion = torch.nn.MSELoss(size_average=False)
#model.parameters()用于检查模型中所能进行优化的张量
#learningrate(lr)表示学习率
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)             ##构造损失函数和优化器


for epoch in range(1000):
    #前馈计算y_pred
    y_pred = model(x_data)
    #前馈计算损失loss
    loss = criterion(y_pred, y_data)
    #打印调用loss时，会自动调用内部__str__()函数，避免产生计算图
    print(epoch, loss)
    #梯度清零
    optimizer.zero_grad()
    #梯度反向传播，计算图清除
    loss.backward()
    #根据传播的梯度以及学习率更新参数
    optimizer.step()                                               

#Output
print('w = ', model.linear.weight.item())
print('b = ', model.linear.bias.item())


#TestModel
x_test = torch.Tensor([[4.0]])                                      ##训练
y_test = model(x_test)


print('y_pred = ', y_test.data)









#######################################################################################




## 线性回归的简洁实现

# 生成数据集

# import numpy as np
# import torch
# from torch.utils import data
# from d2l import torch as d2l

# true_w = torch.tensor([2, -3.4])            # #true_w是个2行1列的矩阵，是个列向量
# true_b = 4.2
# features, labels = d2l.synthetic_data(true_w, true_b, 1000) 


# # 读取数据集

# # 我们可以调用框架中现有的API来读取数据。 我们将features和labels作为API的参数传递，
# # 并通过数据迭代器指定batch_size。 此外，布尔值is_train表示是否希望数据迭代器对象在每个迭代周期内打乱数据。


# def load_array(data_arrays, batch_size, is_train=True):  #@save
#     """构造一个PyTorch数据迭代器"""
#     dataset = data.TensorDataset(*data_arrays)
#     return data.DataLoader(dataset, batch_size, shuffle=is_train)

# batch_size = 10
# data_iter = load_array((features, labels), batch_size)
# print(next(iter(data_iter)))


# ###定义模型

# # nn是神经网络的缩写
# from torch import nn

# net = nn.Sequential(nn.Linear(2, 1))

# ##初始化模型参数

# net[0].weight.data.normal_(0, 0.01)
# net[0].bias.data.fill_(0)


# ##定义损失函数

# loss = nn.MSELoss()


# ##定义优化算法

# trainer = torch.optim.SGD(net.parameters(), lr=0.03)


# ##训练


# num_epochs = 3
# for epoch in range(num_epochs):
#     for X, y in data_iter:
#         l = loss(net(X) ,y)
#         trainer.zero_grad()
#         l.backward()
#         trainer.step()
#     l = loss(net(features), labels)
#     print(f'epoch {epoch + 1}, loss {l:f}')
    
    
# w = net[0].weight.data
# print('w的估计误差：', true_w - w.reshape(true_w.shape))
# b = net[0].bias.data
# print('b的估计误差：', true_b - b)