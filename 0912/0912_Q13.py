n = int(input("请输入你要进行阶乘计算的数："))
i = 1
sum = 1
while i <= n:
    sum *= i
    i += 1
print(f"{n}的阶乘是{sum}")