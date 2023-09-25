# 牛顿法求2^（1/2）
def Square_root_3(c):
    g=c/2
    i=0
    while(abs(g*g-c)>0.00000000001):
        g=(g+c/g)/2
        i+=1
        print("%d:g=%.13f" % (i,g))

Square_root_3(int(input("请输入你要计算的c:")))