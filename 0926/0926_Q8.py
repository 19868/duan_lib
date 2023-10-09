import random
import time

# 选择排序算法
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 归并排序算法
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    while left:
        result.append(left[0])
        left = left[1:]
    while right:
        result.append(right[0])
        right = right[1:]

    return result

# 冒泡排序算法
def bubble_sort(arr):
    n=len(arr)
    if n <= 1:
        return

    for i in range(n):
        is_made_swap=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                is_made_swap=True
        if not is_made_swap:
            break

# 测试排序算法的运行时间
def test_sort(sort, arr):
    start_time = time.time()
    sort(arr)
    end_time = time.time()
    use_time = end_time - start_time
    return use_time

# 生成具有不同长度的随机数列，并测试排序算法的运行时间
lengths = [1000, 2000, 3000, 4000, 5000]
for length in lengths:
    # 生成随机数列
    random_list = [random.randint(1, 1000) for i in range(length)]

    # 测试选择排序的运行时间
    selection_time = test_sort(selection_sort, random_list.copy())

    # 测试归并排序的运行时间
    merge_time = test_sort(merge_sort, random_list.copy())

    # 测试冒泡排序的运行时间
    bubble_time = test_sort(bubble_sort, random_list.copy())

    print(f"Length: {length}")
    print(f"Selection Sort Time: {selection_time:.6f} seconds")
    print(f"Merge Sort Time: {merge_time:.6f} seconds")
    print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
    print()
