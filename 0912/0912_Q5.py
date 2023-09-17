print("请输入三个数x,y,z")
x = int(input("请输入x的值:"))
y = int(input("请输入y的值:"))
z = int(input("请输入z的值:"))
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print("从小到大的顺序为:", x, y, z)