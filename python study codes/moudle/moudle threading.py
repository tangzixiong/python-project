
### Python多线程编程——threading模块

# 使用多线程编程可降低程序的复杂度，使程序更简洁高效。线程是程序执行流的最小单元，是进程的一个实体，
# 一个进程可以拥有多个线程，多个线程可以共享进程所拥有的资源。

# 线程可以提升程序的整体性能，一般分为内核线程和用户线程，内核线程由操作系统内核创建和撤销，
# 用户线程不需要内核支持， 是在用户程序中实现的线程。
# 需要注意的是：线程不能独立运行，他必须依附于进程；线程可以被抢占（中断）和暂时搁置（休眠）。





# 因为 python 解释器使用了内部的全局解释器锁（GIL锁），使得在无论何时计算机只会允许在处理器上运行单个线程，
# 即便多核GPU也是如此（即GIL锁同一时刻只允许一个进程只有一个线程被CPU调度），所以它的效率较其他语言低。



## threading模块的函数

    # threading.active_count()	    返回正运行的线程数量（包括主线程），与len(threading.enumerate())结果相同
    # threading.current_thread()	返回当前线程的变量
    # threading.main_thread()	    返回主线程
    # threading.enumerate()         返回一个正在运行的线程的列表
    



## 创建线程——start()方法

# 在创建线程时必须先定义一个继承threading.Thread的类，
# 然后重写子类中的run()方法，使用start()方法启动线程。

import threading
class threadTest(threading.Thread):              #类必须继承threading.Thread
    
    def __init__(self, args) -> None:            #args为传入线程的参数，可根据自己的需求进行定义
        
        super(threadTest, self).__init__()      #初始化super()内的必须与类名一样
        self.args = args
    
    def run(self) -> None:                      #定义run()方法，主要写线程的执行内容
        print('test thread running......')
        print('args:', self.args)
        return super().run()
    
if __name__ == '__main__':
    test = threadTest('just test')              #实例化
    test.start()                                #启动线程，即运行run()方法
        
        
        
# ##使用函数的方式创建线程
import threading

def threadTest(arg):
    print('test thread running......')
    print('args:', arg)
    

if __name__ == '__main__':
    # target 传入函数名，注意不要写参数； args target传入的函数需要传入的参数，注意传入参数以元组的形式
    thread = threading.Thread(target=threadTest, args=('just test',))
    thread.start()                              #启动线程
    
    
#除 start() 方法外，threading.Thread类还提供了以下方法

    # join(timeout)	        表示主线程等待子线程timeout时长（s）后子线程若还未结束，就强制结束子线程，不设置则主线程会一直等待子线程结束后再结束
    # getName()	            获取线程名
    # setName()	            设置线程名
    # isAlive()	            返回线程是否正在运行
    # ident()	            获取线程标识符
    # setDaemon(bool)	    设置主，子线程运行时的关系。bool为True时主线程结束，子线程立即结束；为false主，子线程运行毫不相关，独立运行

# 原文链接：https://blog.csdn.net/youngwyj/article/details/124720041



##线程同步
# 线程同步是多线程中很重要的概念，当多个线程需要共享数据时，如果不使用线程同步，
# 就会存在数据不同步的情况。要做到线程同步有两种方法，线程锁和条件变量Condition。


### 线程锁
## 1.Lock锁

import threading
import time

num = 0
lock = threading.Lock()     #申请线程锁

class threadTest(threading.Thread):     #类必须继承threading.Thread
    
    def __init__(self) -> None:         # args为传入线程的参数，可根据自己的需求进行定义
        super(threadTest, self).__init__()          #初始化super()内的必须与类名一样
        
    def run(self) -> None:              #定义run()方法， 主要写线程的执行内容
        
        global num                      #声明全局变量num
        
        # lock.acquire()      申请线程锁
        
        print('子线程' + self.getName() + '开始：' + str(time.time()))
        while num < 5:
            time.sleep(2) 
            print(self.getName(), 'num:', num)
            num +=1
        #休眠2s
        print('子线程' + self.getName() + '结束：' + str(time.time()))
        
        #lock.release()     #释放线程锁
        
        return super().run()

if __name__ == '__main__':
    
    print('主线程开始：%s' %(str(time.time())))
    thread1 = threadTest()
    thread1.setName('Thread-1')     #设置线程名称
    thread2 = threadTest()
    thread2.setName('Thread-2')     #设置线程名称
    thread1.start()                 #启动线程
    thread2.start()
    time.sleep(1)
    thread1.join()
    thread2.join()
    print('主线程已结束：%s' %(str(time.time())))
    
    
    
## 2. RLock锁
# RLock锁又称递归锁，其与Lock锁的差别在于，Lock锁只允许在同一线程中申请一次，
# 否则线程会进入死锁，但是RLock允许在同一线程多次调用。


#使用Lock锁产生死锁示例代码

import threading
import time

print('主线程开始：%s' %(str(time.time())))
lock = threading.Lock()

lock.acquire()      #申请线程锁
print(threading.enumerate())

lock.acquire()      #再次申请线程锁，产生了死锁
print(threading.enumerate())

lock.release()
lock.release()
print('主线程结束： %s' %(str(time.time())))



#使用RLock锁不会产生死锁

import threading
import time

print('主线程开始：%s' % (str(time.time())))
lock = threading.RLock()

lock.acquire()              #申请线程锁
print(threading.enumerate())

lock.acquire()              #再次申请线程锁，不会产生死锁
print(threading.enumerate())

lock.release()
lock.release()
print('主线程结束：%s' %(str(time.time())))



##线程锁需要成对出现


###条件变量Condition

#Condition是python3中一种更高级的锁，除和线程锁类似的 acquire() 和 release() 函数外，还提供以下函数。

    # 函数	                说明
    # wait()	        使线程挂起
    # notify()	    唤醒挂起的线程使其运行
    # notifyAll()	唤醒所有线程使其运行
    
    
# https://blog.csdn.net/youngwyj/article/details/124833126