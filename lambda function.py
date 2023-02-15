#用匿名函数，求三个数的乘积及列表元素的值
f = lambda x, y, z: x*y*z
L = lambda x: [x**2, x**3, x**4]
print(f(3,4,5))
print(L(2))

#lambda 函数的语法只包含一个语句： lambda [arg1 [,arg2,.....argn]]: expression

print("-------------------------------------")

sum = lambda arg1, arg2: arg1 + arg2

print("相加后的值为: ", sum(10, 20))
print("相加后的值为: ", sum(20, 20))
