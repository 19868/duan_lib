def fn(n):
    l=[]
    a = n//3
    b = n%3
    if n <= 0:
        print("请输入正确的正整数！")
    elif n < 3:
        l.append(n)
    else:
        for i in range(a-1):
            l.append(3)
        if b==0:
            l.append(3)
        elif b==1:
            l.append(2)
            l.append(2)
        elif b==2:
            l.append(3)
            l.append(2)
    print(l)
n = int(input("请输入一个正整数n:"))
fn(n)


