l = []
for i in range(4):
    a = int(input(f"请输入第{i+1}个数："))
    l.append(a)
l.sort(reverse=True)
print("这四个数从大到小为：")
for item in l:
    print(item)