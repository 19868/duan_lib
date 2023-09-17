flag = 0
s = input("请输入你要判断的字符串：")
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        flag = 1
        break
if flag == 0:
    print("no")
else:
    print("yes")