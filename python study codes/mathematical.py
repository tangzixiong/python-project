#创建和使用小数对象
#小数对象使用decimal模块中的Decimal函数来创建

from decimal import Decimal   
a = Decimal('0.3')+Decimal('0.3')+Decimal('0.3')+Decimal('0.1')
print(a)
print(type(a))

print('------------------------------------------------------------------------')


#小数的全局精度，使用decimal模块中的上下文对象设置小数的全局精度

import decimal
print(Decimal('1')/Decimal('3'))


decimal.getcontext().prec=5         #设置全局小数精度为5位有效数字

print(Decimal('1')/Decimal('3'))
print(Decimal('10')/Decimal('3'))


print('------------------------------------------------------------------------')

#小数的临时精度， 利用with语句创建临时的上下文对象，以设置临时的小数精度
import decimal
print(Decimal('1')/Decimal('3'))                #用默认全局小数精度计算

with decimal.localcontext() as local:
    local.prec = 3                              #设置临时小数精度为三位有效数字
    print(Decimal('1')/Decimal('3'))
    print(Decimal('10')/Decimal('3'))



#分数， 使用fractions模块中的Fraction函数来创建

from fractions import Fraction
x = Fraction(2, 8)
print(x)
print(x+2)
print(x-2)

#可使用Fraction.from_float函数将浮点数转换为分数

b = Fraction.from_float(1.25)
print(b)

print('------------------------------------------------------------------------')


#数学函数

print(abs(-2))                  #求绝对值

print(bin(5))                   #将整数转换为二进制字符串   0b101

print(hex(20))                  #返回整数的十六进制字符串   0x14

print(oct(20))                  #返回整数的八进制字符串     0o24

print(chr(65))                  #返回整数对应ASCII码的字符 

print(ord('A'))                 #返回字符的ASCII码对应的整数

print(divmod(9,4))              #返回商和余数


a = 5; print(eval('a*a+1'))     #返回字符串中表达式的值

print(pow(2, 3))                #pow(x,y)返回x的y次方，x**y

print(round(1.56))              #四舍五入

print(round(1.567,2))           #四舍五入：保留指定位数的小数

print(round(1.5),round(-1.5))