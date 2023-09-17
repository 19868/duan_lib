def cubic_root(n):
    epsilon = 0.0000000001   # 精度控制
    low = 0
    high = n / 2 + 1
    while low <= high:
        mid = (low + high) / 2
        mid_cubed = mid * mid * mid
        if abs(mid_cubed - n) <= epsilon:
            return mid
        elif mid_cubed < n:
            low = mid
        else:
            high = mid
num = int(input("请输入你要进行计算的数："))
result = cubic_root(num)
print(f"The cubic root of %.3f is: %.3f" % (num, result))
