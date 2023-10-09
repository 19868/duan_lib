import random
# 随机生成一个n=10的数组A
A = random.sample([i for i in range(1,100)],10)
B=[]
a=1
for i in range(len(A)):
    for j in range(len(A)):
        if j==i:
            continue  # 若下标相同，则跳过
        a*=A[j]  # 其余每一项累乘
    B.append(a)
    a=1
print('A=',A)
print('B=',B)