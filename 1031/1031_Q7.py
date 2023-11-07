import matplotlib.pyplot as plt
import numpy as np

# 1.散点图：在Matplotlib中，可以使用scatter()函数绘制散点图
# 以下生成一个包含100个随机点的散点图

# 生成随机数据
x = np.random.rand(100)
y = np.random.rand(100)

# 绘制散点图
plt.scatter(x, y)

# 显示图形
plt.show()

# 2.折线图：在Matplotlib中，可以使用plot()函数绘制折线图
# 以下生成一个sin函数的折线图

# 生成随机数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制折线图
plt.plot(x, y)

# 显示图形
plt.show()

# 3.条形图：在Matplotlib中，可以使用bar()函数绘制条形图
# 以下会生成一个包含5个随机高度的条形图

# 生成随机数据
x = ['A', 'B', 'C', 'D', 'E']
y = np.random.randint(1, 10, 5)

# 绘制条形图
plt.bar(x, y)

# 显示图形
plt.show()

