##链表（linked list)
##链表是一种线性表，不像顺序表一样连续存储数据，而是在每个结点(数据存储单元)里存放一个节点的位置信息(地址)

#表元素elem用来存放具体的数据
#连接域next用来存放下一个节点的位置
#变量p指向链表的头节点(首节点)的位置，从p出发能找到表中的任意节点

#节点实现

class SingleNode(object):
    """ 单链表的节点 """
    def __init__(self,item):
        #item存放数据元素
        self.item = item
        #next是下一个节点的标识
        self.next = None
        
        
##单链表的操作
#is_empty()链表是否为空
#length() 链表长度
#travel() 遍历整个链表
#add(item) 链表头部添加元素
#append(item) 链表尾部添加元素
#insert(pos,item)指定位置pos添加元素
#remove(item) 删除节点
#search(item) 查找节点是否存在


#单链表的实现

class SingleLinkList(object):
    """ 单链表 """
    def __init__(self):
        self._head = None
        
    def is_empty(self):
        """ 判断链表是否为空 """
        return self.self._head == None
    
    def length(self):
        """ 链表长度 """
        #cur初始时指向头节点
        cur = self._head
        count = 0
        #尾节点指向None, 当到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count
    def travel(self):
        """ 遍历链表 """
        cur = self._head
        while cur != None:
            print(cur.item, end=" ")
            cur = cur.next
        print("")
        
        
#单链表 链表尾部添加元素，尾插法（append）

    def append(self, item):
        """ 链表尾部添加元素 """
        node = SingleNode(item)
        #先判断链表是否为空，若空则将_head指向新节点
        if self.is_empty():
            self.__head = node
            #若不为空，则找到尾部，将节点的next指向新节点
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node


    #头部添加元素
    def add(self, item):
        """ 头部添加元素 """
        #先创建一个保存item值的节点
        node = SingleNode(item)
        #将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self._head
        #将链表的头_head指向新节点
        self._head = node



#指定位置添加元素
    def insert(self, pos, item):
        """ 指定位置添加元素 """
        #若指定位置pos为第一个元素之前，则执行头部插入
        if pos <=0:
            self.add(item)
        #若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length()-1):
            self.append(item)
        #找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            #pre用来指向指定位置pos的前一个位置pos-1, 初始从头节点开始移动到指定位置
            pre = self._head
            while count < (pos-1):
                count +=1
                pre = pre.next
            #先将新节点node的next指向插入位置的节点
            node.next = pre.next
            #将插入位置的前一个节点的next指向新节点
            pre.next = node


#查找节点是否存在

    def search(self, item):
        """ 链表查找节点是否存在，并返回True或者False """
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False



######测试
if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2,4)
    print("length:",ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(5))
    ll.remove(1)
    print("length", ll.length())
    ll.travel()

