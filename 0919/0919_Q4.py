# 笨方法求解2^（1/2）
def Square_root_1():
    c=2
    i=0
    g=0
    for j in range(0,c+1):
        if(j*j>c and g==0):
            g=j-1
            break
    while(abs(g*g-c)>0.0001):
        g+=0.00001
    print("g=%.5f"%(g))

Square_root_1()