##Linear regression

import numpy as np
import matplotlib.pyplot as plt

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

def forward(x):
    return x * w

def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) * (y_pred - y)

w_list = []
mse_list = []
for w in np.arange(0.0, 4.1, 0.1):
    print('w=', w)
    l_sum = 0
    for x_val, y_val in zip(x_data, y_data):
        y_pred_val = forward(x_val)
        loss_val = loss(x_val, y_val)
        l_sum += loss_val
        print('\t', x_val, y_val, y_pred_val, loss_val)
    print('MSE=', l_sum / 3)
    w_list.append(w)
    mse_list.append(l_sum / 3)


# plt.plot(w_list, mse_list)
# plt.ylabel('Loss')
# plt.xlabel('w')
# plt.show()


print('\n-------------------------------------------------------\n')


##生成数据集

import random
import torch
from d2l import torch as d2l

def synthetic_dataL(w, b, num_examples):        #@save
    """ 生成y=Xw+b+噪声 """
    X = torch.normal(0, 1, (num_examples, len(w)))
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))

true_w = torch.tensor([2, -3.4])
true_b = 4.2
features, labels = synthetic_dataL(true_w, true_b, 1000)
#features中的每一行都包含一个二维数据样本,labels中的每一行都包含一维标签值（一个标量）
print('features:', features[0], '\nlabel:', labels[0])
d2l.set_figsize()
d2l.plt.scatter(features[:, 1].detach().numpy(), labels.detach().numpy(), 1);
d2l.plt.show()




print('\n-------------------------------------------------------\n')


#  训练模型时要对数据集进行遍历，每次抽取一小批量样本，并使用它们来更新我们的模型。
#  由于这个过程是训练机器学习算法的基础，所以有必要定义一个函数，
#  该函数能打乱数据集中的样本并以小批量方式获取数据

def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    # 这些样本是随机读取的，没有特定的顺序
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = torch.tensor(
            indices[i: min(i + batch_size, num_examples)])
        yield features[batch_indices], labels[batch_indices]
        
batch_size = 10

for X, y in data_iter(batch_size, features, labels):
    print(X, '\n', y)
    break