import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
 
# 创建三维图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
 
# 生成数据
x = np.arange(5)
y = np.arange(5)
x, y = np.meshgrid(x, y)
z = np.array([[4, 6, 0, 6, 5],
              [0, 3, 2, 1, 0],
              [7, 5, 0, 5, 7],
              [0, 1, 2, 3, 0],
              [5, 6, 0, 6, 4]])
 
# 绘制曲面图
ax.plot_surface(x, y, z)
 
# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

 
# 显示图形
plt.show()