
##队列(queue)是只允许在一端进行插入操作，而在另一端进行删除操作的线性表

#队列是一种先进先出的（First In First Out）的线性表，简称FIFO。允许插入的一端为队尾，
#允许删除的一端为队头。队列不允许在中间部位进行操作, 同栈一样，队列也可以用顺序表或者链表实现。

#操作
#Queue() 创建一个空的队列
#enqueue(item)往队列中添加一个item元素
#dequeue()从队列头部删除一个元素
#is_empty()判断一个队列是否为空
#size()返回队列的大小


class Queue(object):
    """ 队列 """
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        """ 进队列 """
        self.items.insert(0, item)

    def dequeue(self):
        """ 出队列 """
        return self.items.pop()
    
    def size(self):
        """ 返回大小 """
        return len(self.items)
    
if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("itcast")
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())      



##双端队列(deque, double-ended queue), 是一种具有队列和栈的性质的数据结构

#双端队列中的元素可以从两端弹出，其限定插入和删除操作在表的两端进行。双端队列
#可以在队列任意一端入队和出队。

##操作
#Deque()创建一个空的双端队列
#add_front(item) 从队头加入一个item元素
#add_rear(item) 从队尾加入一个item元素
#remove_front() 从队头删除一个item元素
#remove_rear()  从队尾删除一个item元素
#is_empty() 判断双端队列是否为空
#size() 返回队列的大小


class Deque(object):
    """ 双端队列 """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """ 判断队列是否为空 """
        return self.items ==[]
    
    def add_front(self, item):
        """ 在队头添加元素 """
        self.items.insert(0, item)

    def add_rear(self, item):
        """ 在队尾添加元素 """
        self.items.append(item)

    def remove_front(self):
        """ 从队头删除元素 """
        return self.items.pop(0)
    
    def remove_rear(self):
        """ 从队尾删除元素 """
        return self.items.pop()
    
    def size(self):
        """ 返回队列大小 """
        return len(self.items)
    
if __name__ == "__main__":
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print(deque.size())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_rear())
    print(deque.remove_rear())





##########################################################

##列的典型应用之一是模拟需要以 FIFO 方式管理数据的真实场景。首先，让我们看看孩子们的游戏烫手山芋，
# 在这个游戏中，孩子们围成一个圈，并尽可能快的将一个山芋递给旁边的孩子。在某一个时间，
# 动作结束，有山芋的孩子从圈中移除。游戏继续开始直到剩下最后一个孩子。

# 我们将模拟这个烫山芋的过程。我们的程序将输入名称列表和一个称为 num 常量用于报数。
# 它将返回以 `num` 为单位重复报数后剩余的最后一个人的姓名。为了模拟这个圈，我们使用队列。
# 假设拿着山芋的孩子在队列的前面。当拿到山芋的时候，这个孩子将先出列再入队列，把他放在队列的最后。
# 经过 num 次的出队入队后，前面的孩子将被永久移除队列。并且另一个周期开始，继续此过程，直到只剩下一个名字（队列的大小为 1）。

from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David", "Susan", "Jane", "Kent", "Brad"],7))


