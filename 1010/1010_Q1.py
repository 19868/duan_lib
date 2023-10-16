def Is_prime(n):
    i=2
    flag=1
    if n<2:
        flag=0
    while i*i<=n:
        if a%i==0:
            flag=0
            break
        i+=1
    return flag

a=int(input("请输入你要判断的数："))
if Is_prime(a)==1:
    print(f"{a}是质数")
else:
    print(f"{a}不是质数")