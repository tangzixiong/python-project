
##多维特征输入问题

# http://biranda.top/Pytorch%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0008%E2%80%94%E2%80%94%E5%A4%9A%E7%BB%B4%E7%89%B9%E5%BE%81%E9%97%AE%E9%A2%98/#%E5%A4%9A%E7%BB%B4%E7%89%B9%E5%BE%81%E8%BE%93%E5%85%A5%E9%97%AE%E9%A2%98


import torch
import numpy as np
#读取文件，一般GPU只支持32位浮点数
xy = np.loadtxt("diabetes.csv", delimiter=',', dtype = np.float32)
#-1行-1列不取
x_data = torch.from_numpy(xy[:-1, :-1])
#单取-1列作为矩阵
y_data = torch.from_numpy(xy[:-1, [-1]])
#取-1行的测试集部分
test_data = torch.from_numpy(xy[[-1], :-1])
pred_test = torch.from_numpy(xy[[-1],[-1]])
class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = torch.nn.Linear(8, 6)
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.sigmoid(self.linear1(x))
        x = self.sigmoid(self.linear2(x))
        x = self.sigmoid(self.linear3(x))
        return x

model = Model()

criterion = torch.nn.BCELoss(size_average=True)

optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

for epoch in range(1000):
    #Forward 并非mini-batch的设计，只是mini-batch的风格
    y_pred = model(x_data)
    loss = criterion(y_pred,y_data)
    print(epoch, loss.item())

    #Backward
    optimizer.zero_grad()
    loss.backward()

    #Update
    optimizer.step()

print("test_pred = ", model(test_data).item())
print("infact_pred = ", pred_test.item())