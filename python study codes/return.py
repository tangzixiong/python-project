# return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。    

def sum( arg1, arg2 ):
    # 返回两个参数的和
    total = arg1 + arg2
    print( "函数内：", total)
    return total

total = sum(10, 20)
print("函数外：", total)



