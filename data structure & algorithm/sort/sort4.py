
##归并排序

# 归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，
# 再合并数组。将数组分解最小之后，然后合并两个有序数组，基本思路是比较两个数组的
# 最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。然后再比较，直至一个数
# 组为空，最后把另一个数组的剩余部分复制过来即可。


##merge的功能是将前后相邻的两个有序表归并为一个有序表的算法
def merge(left, right):
    """ 合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组 """
    #left与right的下标指针
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    #二分分解
    num = len(alist)//2             #从中间划分两个子序列
    left = merge_sort(alist[:num])  #对左侧子序列进行递归排序
    right = merge_sort(alist[num:]) #对右侧子序列进行递归排序
    # 合并
    return merge(left, right)



alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sorted_alist = merge_sort(alist)
print(sorted_alist)


# 最优时间复杂度：O(nlogn)
# 最坏时间复杂度：O(nlogn)
# 稳定性：稳定