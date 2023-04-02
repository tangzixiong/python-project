
## 反向传播
#http://biranda.top/Pytorch%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0005%E2%80%94%E2%80%94%E5%8F%8D%E5%90%91%E4%BC%A0%E6%92%AD%E7%AE%97%E6%B3%95/


import torch

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]


#赋予tensor中的data
w = torch.Tensor([1.0])
#设定需要计算梯度grad
w.requires_grad = True

#模型y=x*w 建立计算图

def forward(x):
    """ 
    w为Tensor类型
    x强制转换为Tensor类型
    通过这样的方式建立计算图
    """
    return x * w

def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) ** 2

print('predict (before training)', 4, forward(4).item())

for epoch in range(100):
    for x, y in zip(x_data, y_data):
        #创建新的计算图
        l = loss(x, y)
        #进行反馈计算， 此时才开始求梯度， 此后计算图进行释放
        l.backward()
        #grad.item()取grad中的值变成标量
        print('\tgard:', x, y, w.grad.item())
        #单纯的数值计算要用data,不能用张量， 否则会在内部创建新的计算图
        w.data = w.data - 0.01 * w.grad.data
        #把权重梯度里的数据清零
        w.grad.data.zero_()
    print("progress:", epoch, l.item())
    
print('predict (after training)', 4, forward(4).item())