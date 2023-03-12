## decimal 模块

# http://www.ityouknow.com/python/2019/10/21/python-decimal-038.html

# decimal 模块设计以十进制数、算术上下文和信号这三个概念为中心。
# 十进制数是不可变的，它有一个符号，系数数字和一个指数，为了保持重要性，
# 系数数字不会截断尾随零，十进制数也有特殊值，如：Infinity、-Infinity 和 NaN；
# 算术上下文是指定精度、舍入规则、指数限制、指示操作结果的标志以及确定符号是否
# 被视为异常的陷阱启用器的环境；信号是在计算过程中出现的异常条件组

from decimal import *

print(Decimal(1.1) + Decimal(3.3))
print(Decimal(1.1) - Decimal(3.3))
print(Decimal(1.1) * Decimal(3.3))
print(Decimal(1.1) / Decimal(3.3))

# 输出结果
"""
4.399999999999999911182158030
-2.199999999999999733546474090
3.630000000000000097699626167
0.3333333333333333781908292778
"""

# 使用getcontext().prec设定有效数字
from decimal import *

print(Decimal(1.1) / Decimal(3.3))
print((Decimal(1.1) / Decimal(3.3)).quantize(Decimal('0.00')))    #设置小数位数

getcontext().prec = 2
print(Decimal(1.1) / Decimal(3.3))

