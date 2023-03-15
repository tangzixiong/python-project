
##栈(stack)
#有些地方称为堆栈，是一种容器，可存入数据元素、访问元素、删除元素，它的特点在于只能允许
# 在容器的一端（称为栈顶端指标，英语：top）进行加入数据（英语：push）和输出数据（英语：pop）
#的运算。没有了位置概念，保证任何时候可以访问、删除的元素都是此前最后存入的那个元素，确定了
#一种默认的访问顺序。

#由于栈数据结构只允许在一端进行操作，因而按照后进先出（LIFO, Last In First Out）的原理运作。

#栈可以用顺序表实现，也可以用链表实现

##栈的操作
# Stack() 创建一个新的空栈
# push(item) 添加一个新的元素item到栈顶
# pop() 弹出栈顶元素
# peek() 返回栈顶元素
# is_empty() 判断栈是否为空
# size() 返回栈的元素个数


class Stack(object):
    """ 栈 """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """ 判断是否为空 """
        return self.items == []
    def push(self, item):
        """ 加入元素 """
        self.items.append(item)

    def pop(self):
        """ 弹出元素 """
        return self.items.pop()
    
    def peek(self):
        """ 返回栈顶元素 """
        return self.items[len(self.items)-1]
    
    def size(self):
        """ 返回栈的大小 """
        return len(self.items)
    
if __name__ == "__main__":
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())



print('\n------------------------------------------------------------------\n')

# 通过实例化 Stack 类执行 以上stack中的操作。注意，Stack 类的定义是从 pythonds 模块导入的。

from pythonds.basic.stack import Stack

s = Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())





print('\n------------------------------------------------------------------\n')


##  括号匹配
# 从空栈开始，从左到右处理括号字符串。如果一个符号是一个开始符号，将其作为一个信号，
# 对应的结束符号稍后会出现。另一方面，如果符号是结束符号，弹出栈，只要弹出栈的开始
# 符号可以匹配每个结束符号，则括号保持匹配状态。如果任何时候栈上没有出现符合开始符号
# 的结束符号，则字符串不匹配。最后，当所有符号都被处理后，栈应该是空的


from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
    
print(parChecker('((()))'))
print(parChecker('(()'))