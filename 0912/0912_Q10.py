# for循环
L = [1, 2, 3, 4, 5]
for i in range(len(L)-1, -1, -1):
    print(L[i])

# while循环
L = [1, 2, 3, 4, 5]
i = len(L)-1
while i >= 0:
    print(L[i])
    i -= 1