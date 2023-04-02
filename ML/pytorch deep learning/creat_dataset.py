import os 
#下面我们将数据集按行写入CSV文件中
os.makedirs(os.path.join('./ML', 'data'), exist_ok= True)
data_file = os.path.join('./ML', 'data', 'house_tiny.csv')
with open(data_file, 'w') as f:
    f.write('NumRooms, Alley, Price\n')      # 列名
    f.write('NA,Pave,127500\n')              # 每行表示一个数据样本
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA, NA, 140000\n')
    
  
  
#从创建的CSV文件中加载原始数据集，我们导入pandas包并调用read_csv函数
    
import pandas as pd
 
data = pd.read_csv(data_file)
# print(data)

""" 
   NumRooms  Alley   Price
0       NaN   Pave  127500
1       2.0    NaN  106000
2       4.0    NaN  178100
3       NaN     NA  140000
"""

# “NaN”项代表缺失值。 为了处理缺失的数据，典型的方法包括插值法和删除法， 
# 其中插值法用一个替代值弥补缺失值，而删除法则直接忽略缺失值

# 通过位置索引iloc，我们将data分成inputs和outputs， 其中前者为data的前两列，
# 而后者为data的最后一列。 对于inputs中缺少的数值，我们用同一列的均值替换“NaN”项

inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
inputs = inputs.fillna(inputs.mean())
#print(inputs)


""" 
   NumRooms  Alley
0       3.0   Pave
1       2.0    NaN
2       4.0    NaN
3       3.0     NA
"""

# 对于inputs中的类别值或离散值，我们将“NaN”视为一个类别。 由于“巷子类型”（“Alley”）列只接受
# 两种类型的类别值“Pave”和“NaN”， pandas可以自动将此列转换为两列“Alley_Pave”和“Alley_nan”。 
# 巷子类型为“Pave”的行会将“Alley_Pave”的值设置为1，“Alley_nan”的值设置为0。 缺少巷子类型的行
# 会将“Alley_Pave”和“Alley_nan”分别设置为0和1

inputs = pd.get_dummies(inputs, dummy_na=True)
print(inputs)



## 现在inputs和outputs中的所有条目都是数值类型，它们可以转换为张量格式

import torch

X, y = torch.tensor(inputs.values), torch.tensor(outputs.values)
print(X, y,sep='\n')