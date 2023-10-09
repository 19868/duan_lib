def LM(x):
    L = int(x)  # L为十进制整数部分
    M = float(x - L)  # M为十进制小数部分

    # 考虑整数部分
    a1 = 0  # 用于计数
    b1 = L  # 用于while的操作
    c1 = L  # 用于for的操作
    while b1 >= 1:
        b1 = b1 // 2  # 整数部分不断除以2取整
        a1 = a1 + 1  # 计算次数

    d1 = []  # 以字符形式存放整数部分的二进制
    e1 = 0
    for i in range(a1):
        e1 = c1 % 2
        d1.append(str(int(e1)))
        c1 = (c1 - e1) / 2
    d1.reverse()

    # 考虑小数部分
    a2 = M
    b2 = []
    while True:
        a2 = a2 * 2
        if a2 >= 1.0:
            b2.append("1")
            a2 = a2 - 1
            continue
        elif 0 < a2 < 1.0:
            b2.append("0")
            continue
        else:
            break
    b2.insert(0, ".")  # 在起始位置插入小数点

    b = d1 + b2  # 整数部分和小数部分连接

    result = "".join(b)  # 连接列表中的各个字符（中间分隔符为空）
    return result


x = float(input('请输入您要转化的十进制数：'))
print('其对应的二进制数为：', LM(x))