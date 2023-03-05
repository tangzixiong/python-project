##排序算法(sorting algorithm)是一种能将一串数据依照特定顺序进行排列的一种算法

#稳定性：稳定排序算法会让原本有相等键值的纪录维持相对次序。也就是如果一个排序算法
#是稳定的，当有两个相等键值的纪录R和S，且在原本的列表中R出现在S之前，在排序过的列
#表中R也将会是在S之前。


##冒泡排序(Bubble Sort)
#重复地遍历要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。遍历数列的工作是
#重复地进行直到没有再需要交换，也就是说该数列已经排序完成。越小的元素会经由交换慢慢“浮”到数列的顶端。



## 冒泡排序算法的运作如下：

# 比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
# 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
# 针对所有的元素重复以上的步骤，除了最后一个。
# 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。


def bubble_sort(alist):
    for j in range(len(alist)-1, 0, -1):
        # j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(li)
print("冒泡排序：", li)


# import timeit

# def time_sort():

#     li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#     def bubble_sort(alist):
#         for j in range(len(alist)-1, 0, -1):
#             # j表示每次遍历需要比较的次数，是逐渐减小的
#             for i in range(j):
#                 if alist[i] > alist[i+1]:
#                     alist[i], alist[i+1] = alist[i+1], alist[i]

# time = timeit.Timer("time_sort", "from __main__ import time_sort")

# print(time.timeit())



#时间复杂度 ： 最优O(n), 最坏O(n^2)  稳定


######################################################################


##选择排序(Selection sort)

#首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中
# 继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。


def selection_sort(alist):
    n = len(alist)
    #需要进行n-1次选择操作
    for i in range(n-1):
        #记录最小位置
        min_index = i
        # 从i+1位置到末尾选择出最小数据
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        # 如果选择出的数据不在正确位置，进行交换
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]

alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
selection_sort(alist)
print("选择排序:", alist)





# import timeit
# def time2_sort():
#     alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
#     def selection_sort(alist):
#             n = len(alist)
#             #需要进行n-1次选择操作
#             for i in range(n-1):
#                 #记录最小位置
#                 min_index = i
#                 # 从i+1位置到末尾选择出最小数据
#                 for j in range(i+1, n):
#                     if alist[j] < alist[min_index]:
#                         min_index = j
#                 # 如果选择出的数据不在正确位置，进行交换
#                 if min_index != i:
#                     alist[i], alist[min_index] = alist[min_index], alist[i]

# time2 = timeit.Timer("time2_sort", "from __main__ import time2_sort")

# print(time2.timeit())



# 时间复杂度:最优：O(n^2)  最坏：O(n^2)
# 稳定性：不稳定（考虑升序每次选择最大的情况）



#########################################################################

##插入排序(Insertion Sort)
#是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序
# 在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。


def insert_sort(alist):
    #从第二个位置， 即下标为1的元素开始向前插入
    for i in range(1, len(alist)):
        #从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insert_sort(alist)
print("插入排序: ", alist)


##时间复杂度 ； O(n)（升序排列，序列已经处于升序状态）最坏O(n^2) 稳定性：稳定