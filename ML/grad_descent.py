
import numpy as np
import matplotlib.pyplot as plt

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = 1.0

def forward(x):
    return x * w

def cost(xs, ys):
    cost=0
    for x, y in zip(xs, ys):        
# zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，
# 将对象中对应的元素打包成一个个tuple（元组）,然后返回由这些tuples组成的list（列表）
        y_pred = forward(x)
        cost += (y_pred-y) **2
    return cost / len(xs)
        
def gradient(xs, ys):
    grad = 0
    for x, y in zip(xs, ys):
        grad += 2 * x * (x * w - y)
    return grad / len(xs)

print('Predict (before training)', 4, forward(4))

cost_list = []

for epoch in range(100):
    cost_val = cost(x_data, y_data)
    cost_list.append(cost_val)
    grad_val = gradient(x_data, y_data)
    w -= 0.01 * grad_val
    print('Epoch:', epoch, "w=" , w, "loss=" , cost_val)
print('Predict (after training)', 4, forward(4))


plt.plot(range(100), cost_list)
plt.plot(np.array(cost_list), color="r", marker='.')
plt.ylabel('cost')
plt.xlabel('epoch')
plt.show()


#####################################################################

##随机梯度下降

# import numpy as np
# import matplotlib.pyplot as plt

# x_data = [1.0, 2.0, 3.0]
# y_data = [2.0, 4.0, 6.0]

# w = 1.0
# #前馈计算
# def forward(x):
#     return x * w
# #求MSE
# def loss(x, y):
#     y_pred = forward(x)
#     return (y_pred-y) ** 2
# #求梯度
# def gradient(x, y):
#     return 2*x*(x*w-y)

# _cost = []
# for epoch in range(100):
#     for x, y in zip(x_data, y_data):
#         grad_val = gradient(x, y)
#         w -= 0.01*grad_val
#         cost_val = loss(x, y)
#         _cost.append(cost_val)
           
#     print("progress: ",epoch, "W= ", w, "loss = ", cost_val)
# print("Predict(after training)",4,forward(4))

# #绘图
# plt.plot(_cost,range(100))
# plt.ylabel("Cost")
# plt.xlabel('Epoch')
# plt.show()