
##加载数据集

#http://biranda.top/Pytorch%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0009%E2%80%94%E2%80%94%E5%85%B3%E4%BA%8E%E6%95%B0%E6%8D%AE%E9%9B%86/#%E6%95%B0%E6%8D%AE%E9%9B%86

import torch
import numpy as np
from torch.utils.data import Dataset            #Dataset是抽象类， 无法实例化
from torch.utils.data import DataLoader         #DataLoader可实例化

class DiabetesDataset(Dataset):
    def __init__(self, filepath):
        xy = np.loadtxt(filepath, delimiter=',', dtype=np.float32)
        #获得数据集长度
        self.len = xy.shape[0]
        self.x_data = torch.from_numpy(xy[:, :-1])
        self.y_data = torch.from_numpy(xy[:, [-1]])
        
    #获得索引方法
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    #获得数据集长度
    def __len__(self):
        return self.len

dataset = DiabetesDataset('D:\git space\git-demo\ML\data\diabetes.csv')
#num_workers表示多线程的读取
train_loader = DataLoader(dataset=dataset, batch_size=32, shuffle=True, num_workers=2)

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

if __name__ =='__main__':
    for epoch in range(2):
        #enumerate: 可获得当前迭代的次数
        for i, data in enumerate(train_loader, 0):
            #准备数据dataloader会将batch_size返回的数据整合成矩阵加载
            inputs, labels = data
            #前馈
            y_pred = model(inputs)
            loss = criterion(y_pred, labels)
            print(epoch, i, loss.item())
            #反向传播
            optimizer.zero_grad()
            loss.backward()
            #更新
            optimizer.step()