

# import numpy as np
# import matplotlib.pyplot as plt

# x_data = [1.0, 2.0, 3.0]
# y_data = [2.0, 4.0, 6.0]

# cost_list = []
# w = 1.0

# def forward(x):
#     return x * w

# def cost(xs, ys):
#     cost=0
#     for x, y in zip(xs, ys):        
# # zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，
# # 将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）
#         y_pred = forward(x)
#         cost += (y_pred-y) **2
#     return cost / len(xs)
        
# def gradient(xs, ys):
#     grad = 0
#     for x, y in zip(xs, ys):
#         grad += 2 * x * (x * w - y)
#     return grad / len(xs)

# print('Predict (before training)', 4, forward(4))




# for epoch in range(100):
#     cost_val = cost(x_data, y_data)
#     grad_val = gradient(x_data, y_data)
#     w -= 0.01 * grad_val
#     print('Epoch:', epoch, "w=" , w, "loss=" , cost_val)
# print('Predict (after training)', 4, forward(4))


# cost_list.append(cost_val)


# plt.plot(epoch, cost_list)
# plt.ylabel('cost')
# plt.xlabel('epoch')
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]
_cost = []
w = 1.0
#前馈计算
def forward(x):
    return x * w
#求MSE
def cost(xs, ys):
    cost = 0
    for x, y in zip(xs,ys):
        y_pred = forward(x)
        cost += (y_pred-y) ** 2
    return cost/len(xs)
#求梯度
def gradient(xs, ys):
    grad = 0
    for x, y in zip(xs,ys):
        temp = forward(x)
        grad += 2*x*(temp-y)
    return grad / len(xs)

for epoch in range(100):
     cost_val = cost(x_data, y_data)
     _cost.append(cost_val)
     grad_val = gradient(x_data, y_data)
     w -= 0.01*grad_val
     print("Epoch: ",epoch, "w = ",w ,"loss = ", cost_val)
print("Predict(after training)",4,forward(4))

#绘图
plt.plot(_cost,range(100))
plt.ylabel("Cost")
plt.xlabel('Epoch')
plt.show()