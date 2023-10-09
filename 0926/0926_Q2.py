import random
n = int(input("请输入你要产生的10-20的随机浮点数的个数："))
i = 0
while i < n:
    print(random.uniform(10,20))
    i+=1