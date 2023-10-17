import random
import math
def func(times):
    sum=0
    for i in range(times):
        x = random.uniform(2,3)
        y = random.uniform(0,45)
        d=x*x+4*x*math.sin(x)-y
        if d>=0:
            sum+=1
    return(45*sum)/(times)
print(func(1000000))
