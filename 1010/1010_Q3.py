import random

# 插入排序
def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current
    return arr

list = random.sample([i for i in range(1,100)],10)
print(list)
print(insertionSort(list))