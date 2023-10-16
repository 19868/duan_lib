import random

# 希尔排序
'''
时间复杂度：
在最坏的情况下，希尔排序的时间复杂度为O(n^2)
但在平均情况下，其时间复杂度为O(n^1.5)

空间复杂度：
希尔排序的空间复杂度为O(1)，因为它只需要常数级别的额外空间用于存储临时变量。
'''

def shellSort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            j = i
            while j >= gap and arr[j - gap] > arr[j]:
                arr[j] , arr[j - gap] = arr[j - gap] , arr[j]
                j -= gap
        gap //= 2
    return arr

list = random.sample([i for i in range(1,100)],10)
print(list)
print(shellSort(list))