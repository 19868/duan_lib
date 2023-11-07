import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# 1.散点图
# 以下生成一个包含100个随机点的散点图

# 生成随机数据
x = np.random.rand(100)
y = np.random.rand(100)

# 绘制散点图
sns.scatterplot(x=x, y=y)

# 显示图形
plt.show()


# 2.折线图
# 以下生成一个sin函数的折线图

# 生成随机数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制折线图
sns.lineplot(x=x, y=y)

# 显示图形
plt.show()


# 3.条形图
# 以下会生成一个包含5个随机高度的条形图

# 生成随机数据
x = ['A', 'B', 'C', 'D', 'E']
y = np.random.randint(1, 10, 5)

# 绘制条形图
sns.barplot(x=x, y=y)

# 显示图形
plt.show()
