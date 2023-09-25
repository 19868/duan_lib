# 牛顿法求10^（1/3）
def Cubic_root_3():
    c=10
    g=c/2
    i=0
    while(abs(g*g*g-c)>0.00000000001):
        g=(2*g*g*g+c)/(3*g*g)
        i+=1
        print("%d:g=%.13f" % (i,g))

Cubic_root_3()