
##Loist回归

#分类

import torch.nn.functional as F
import torch
#数据作为矩阵参与Tensor

x_data = torch.Tensor([[1.0], [2.0], [3.0]])                        ## 准备数据集                        
y_data = torch.Tensor([[0], [0], [1]])

#改用LogisticRegressionModel 同样继承于Module
class LogisticRegressionModel(torch.nn.Module):
    def __init__(self):
        super(LogisticRegressionModel, self).__init__()
        self.linear = torch.nn.Linear(1, 1)
    
    
    def forward(self, x):
        #对原先的linear结果进行sigmod激活
        y_pred = F.sigmoid(self.linear(x))
        return y_pred

    
model = LogisticRegressionModel()                                     ##设计模型

#构造的criterion对象所接受的参数为（y',y） 改用BCE
criterion = torch.nn.BCELoss(size_average=False)
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
x_test = torch.Tensor([[4.0]])                                       ##训练
y_test = model(x_test)


print('y_pred = ', y_test.data)



####Result of Logistic Regression
import torch
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 200)
x_t = torch.Tensor(x).view((200, 1))            #200行1列
y_t = model(x_t)
y = y_t.data.numpy()
plt.plot(x, y)
plt.plot([0, 10], [0.5, 0.5], c='r')
plt.xlabel('Hours')
plt.ylabel('Probability of Pass')
plt.grid()
plt.show()