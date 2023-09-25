# 牛顿法求2^（1/2）
def Square_root_3_1(c):
    g=c
    i=0
    while(abs(g*g-c)>0.00000000001):
        g=(g+c/g)/2
        i+=1
    print("g=c  %d:g=%.13f" % (i,g))
def Square_root_3_2(c):
    g=c/4
    i=0
    while(abs(g*g-c)>0.00000000001):
        g=(g+c/g)/2
        i+=1
    print("g=c/4  %d:g=%.13f" % (i,g))

Square_root_3_1(int(input("请输入你要计算的c(g=c):")))
Square_root_3_2(int(input("请输入你要计算的c(g=c/4):")))