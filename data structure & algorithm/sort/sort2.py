
##快速排序(Quick sort)  又称划分交换排序(partition-exchange sort)
#通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
#然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。


# 步骤为：
# 1. 从数列中挑出一个元素，称为"基准"（pivot），
# 2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可
# 以到任一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
# 3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

# 递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。虽然一直递归下去，但是这个算法总
# 会结束，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。



# def quick_sort(alist, start, end):
#     """ 快速排序 """

#     #递归的退出条件
#     if start >= end:
#         return 
    
#     #设定起始元素为要寻找位置的基准元素
#     mid = alist[start]

#     #low为序列左边的由左向右移动的游标
#     low = start

#     #high为序列右边的由右向左移动的游标
#     high = end

#     while low < high:
#         #如果low与high 未重合，high指向的元素比基准元素大， 则high向左移动
#         while low < high and alist[high] >= mid:
#             high -= 1

#             #将high指向的元素放到low的位置上
#             alist[low] = alist[high]

#         #如果low与high未重合， low指向的元素比基准元素小，则low向右移动
#         while low < high and alist[low] < mid:
#             low += 1
#             #将low指向的元素放到high的位置上
#             alist[high] = alist[low]

#     #退出循环后， low与high重合， 此时所指位置为基准元素的正确位置
#     #将基准元素放到该位置
#     alist[low] = mid

#     #对基准元素左边的子序列进行快速排序
#     quick_sort(alist, start, low-1)

#     #对基准元素右边的子序列进行快速排序
#     quick_sort(alist, low+1, end)

# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# quick_sort(alist, 0, len(alist)-1)
# print(alist)





########################################################################

# def quick_sort(a, low, high):
#     if low >= high:
#         return a 
#     i = low
#     j = high
#     #定义基准，基准左边小于基数， 右边大于基数
#     pivot = a[low]
#     while i < j:
#         #从后向前扫描
#         while i < j and a[j] > pivot:
#             j -= 1
#         a[i] = a[j]
#         #从前向后扫描
#         while i < j and a[i] < pivot:
#             i += 1
#         a[j] = a[i]
#     a[j] = pivot

#     #分段排序
#     quick_sort(a, low, j-1)
#     quick_sort(a, j+1, high)

#     return a 

# lists=[5, 4, 3, 2, 1]
# quick_sort(lists, 0, len(lists)-1)
# print(alist)



####################################################################

# https://www.techiedelight.com/zh/quicksort/

def swap(A, i, j):

    temp = A[i]
    A[i] = A[j]
    A[j] = temp

#使用 Lomuto 分区方案进行分区
def partition(a, start, end):

    #从列表中选择最右边的元素作为枢轴
    pivot = a[end]

    #小于枢轴 的元素将被推到pIndex的左侧
    #元素超过枢轴将被推到pIndex的右侧
    #平等元素可以去任何一种方式
    pIndex = start

    #每次我们找到一个小于或等于枢轴的元素，
    #pIndex增加，并且该元素将被放置前枢轴
    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, pIndex)
            pIndex = pIndex + 1

    #用枢轴交换pIndex
    swap(a, end, pIndex)

    return pIndex    #枢轴元素的索引

#快速排序
def quicksort(a, start, end):

    #基础条件
    if start >= end:
        return
    #跨枢轴重新排列元素
    pivot = partition(a, start, end)

    #在包含小于主元的元素的子列表上重复出现
    quicksort(a, start, pivot - 1)

    #在包含元素大于枢轴的子列表上重复出现
    quicksort(a, pivot + 1, end)

if __name__ == '__main__':

    a = [9, -3, 5, 2, 6, 8, -6, 1, 3]
    quicksort(a, 0, len(a) - 1)
    print(a)


##时间复杂度： 最优O(nlogn)  最坏O(n^2)  稳定性， 不稳定