# 方法一：蒙特卡罗法
import random

def pi(times):
    sum=0
    for i in range(times):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        d=x*x+y*y
        if d<=1:
            sum+=1
    return(4*sum)/(times)
print(pi(1000000))

# 方法二：BBP公式法
pi=0
N=100
for k in range(N):
	pi+=1/pow(16,k)*(\
		4/(8*k+1)-2/(8*k+4)-\
		1/(8*k+5)-1/(8*k+6))
print("圆周率值是：%.10f"%(pi))


# 方法三：莱布尼茨公式法
result = 0
start = 1
for i in range(1, 10000001):
    if i % 2 == 0:
        result = result - 4/start
        start += 2
    else:
        result = result + 4/start
        start += 2
print(round(result, 10))