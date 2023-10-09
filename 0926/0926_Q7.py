# 辗转相除法求最大公约数
a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))
m = max(a,b)
n = min(a,b)
t = m % n
while t != 0:
    m,n = n,t
    t = m % n
print("最大公约数是%d" % n)