#线性代数

# https://zh-v2.d2l.ai/chapter_preliminaries/linear-algebra.html

## 标量(scalar)

import torch

x = torch.tensor(3.0)
y = torch.tensor(2.0)

#print(x+y, x*y, x/y, x**y, sep='\n') 

""" 
tensor(5.)
tensor(6.)
tensor(1.5000)
tensor(9.)
"""


##向量(vector)

x = torch.arange(4)
#print(x)


""" 
tensor([0, 1, 2, 3])
"""
print(x[3])