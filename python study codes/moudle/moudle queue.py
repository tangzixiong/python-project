## queue模块
# queue 模块即队列，特别适合处理信息在多个线程间安全交换的多线程程序中

# http://www.ityouknow.com/python/2019/10/10/python-queue-029.html

## queue 模块定义了以下四种不同类型的队列，它们之间的区别在于数据入队列之后出队列的顺序不同。


## queue.Queue(maxsize=0)  先进先出FIFO队列
# 入参 maxsize 是一个整数，用于设置队列的最大长度。一旦队列达到上限，插入数据将会被阻塞，
# 直到有数据出队列之后才可以继续插入。如果 maxsize 设置为小于或等于零，则队列的长度没有限制

import queue
q = queue.Queue()       #创建Queue队列
for i in range(3):
    q.put(i)            #在队列中依次插入0, 1, 2元素
for i in range(3):
    print(q.get())      #依次从队列中取出插入的元素, 输出顺序为0 1 2


## queue.LifoQueue(maxsize=0)  后进先出LIFO队列

import queue
q = queue.LifoQueue()       #创建LifoQueue 队列
for i in range(3):
    q.put(i)                #在队列中依次插入0 1 2元素
for i in range(3):
    print(q.get())          #依次从队列中取出插入的元素， 2 1 0



## PriorityQueue(maxsize=0)
# 优先级队列，比较队列中每个数据的大小，值最小的数据拥有出队列的优先权
# 数据一般以元组的形式插入，典型形式为(priority_number, data)。如果队列中
# 的数据没有可比性，那么数据将被包装在一个类中，忽略数据值，仅仅比较优先级数字。

import queue
q = queue.PriorityQueue()       #创建PriorityQueue队列
data1 = (1, 'python')
data2 = (2,'-')
data3 = (3,'100')
style = (data2, data3, data1)
for i in style:
    q.put(i)               #在队列中依次插入元素 data2, data3, data1

for i in range(3):
    print(q.get())         #依次从队列中取出插入的元素，数据元素输出顺序为 data1、data2、data3


##queue.SimpleQueue   先进先出类型的简单队列，没有大小限制

import queue
q = queue.SimpleQueue()         #创建SimpleQueue队列
for i in range(3):
    q.put(i)                    #在队列中依次插入0，1，2元素
for i in range(3):
    print(q.get())              #依次从队列中取出插入的元素， 0， 1， 2


##queue.Empty异常
# 当队列中没有数据元素时，取出队列中的数据会引发queue.Empty异常
# 主要是不正当使用 get() 和 get_nowait() 引起的

import queue
try:
    q = queue.Queue(3)      #设置队列上限为3
    q.put('python')         #在队列中插入字符串 'python'
    q.put('-')              #在队列中插入字符串 '-'
    q.put('100')
    for i in range(4):      ## 从队列中取数据，取出次数为4次，引发 queue.Empty 异常
        print(q.get(block=False))
except queue.Empty:
    print('queue.Empty')


## queue.Full异常
# 当队列数据元素容量达到上限时，继续往队列中放入数据会引发 queue.Empty 
# 异常，主要是不正当使用 put() 和 put_nowait() 引起的。

import queue

try:
    q = queue.Queue(3)
    q.put('python')
    q.put('-')
    q.put('100')
    q.put('stay hungry, stay foolish', block=False)
except queue.Full:
    print('queue.Full')






## task_done，表示队列内的数据元素已经被取出，即每个 get 用于获取一个数据元素， 
# 后续调用 task_done 告诉队列，该数据的处理已经完成。如果被调用的次数多于放入
# 队列中的元素个数，将引发 ValueError 异常。

## join，一直阻塞直到队列中的所有数据元素都被取出和执行，只要有元素添加到 queue 
#  中就会增加。当未完成任务的计数等于0，join 就不会阻塞


import queue
q = queue.Queue()
q.put('python')
q.put('-')
q.put('100')
for i in range(3):
    print(q.get())
    q.task_done()       # 如果不执行 task_done，join 会一直处于阻塞状态，等待 task_done 告知它数据的处理已经完成
q.join()


####################################################################################
#下面是一个经典示例，生产者和消费者线程分别生产数据和消费数据，先生产后消费。采用task_done和join 
# 确保处理信息在多个线程间安全交换，生产者生产的数据能够全部被消费者消费掉。

from queue import Queue
import random
import threading
import time

#生产者线程
class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue
    def run(self):
        for i in range(5):
            print("%s: %s is producing %d to the queue!" %(time.ctime(),self.getName(), i))
            self.data.put(i)                #将生产的数据放入队列
            time.sleep(random.randrange(10)/5)
        print("%s: %s finished!" %(time.ctime(), self.getName()))

#消费者线程
class Consumer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue
    def run(self):
        for i in range(5):
            val = self.data.get()       #拿出已经生产好的数据
            print("%s: %s is consuming. %d in the queue is consumed!" %(time.ctime(),self.getName(), val))
            time.sleep(random.randrange(5))
            self.data.task_done()       #告诉队列有关这个数据的任务已经处理完成
        print("%s: %s finished!" %(time.ctime(), self.getName()))


#主线程
def main():
    queue = Queue()
    producer = Producer('Pro.', queue)
    consumer = Consumer('Con.', queue)
    producer.start()
    consumer.start()
    queue.join()            #阻塞，直到生产者生产的数据全都被消费掉
    producer.join()         #等待生产者结束线程
    consumer.join()         #等待消费者线程结束
    print('All threads terminate!')

if __name__ == '__main__':
    main()