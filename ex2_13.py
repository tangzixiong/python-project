#数据分组

def bifurcate_by(L, fn):
    return [[x for x in L if fn(x)],
        [x for x in L if not fn(x)]]
s = bifurcate_by(['beep', 'boop', 'foo', 'bar',], lambda x: x[0] == 'b')
                            #使用lambda来创建匿名函数，它是一个可以接收任意多个参数并且返回单个表达式值的函数
print(s)