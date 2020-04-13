import matplotlib.pyplot as plt
import numpy as np
#
plt.subplot(121)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = True
data = np.load('国民经济核算季度数据.npz')
np.set_printoptions(threshold=np.inf)
print(data.files)  # 查看数据类型
name = data['columns']  # 提取其中的columns数组，视为数据的标签
values = data['values']  # 提取其中的values数组，数据的存在位置
print(name)
print(values)

plt.xlabel('年份')
plt.ylabel('生成总值（亿元）')
plt.xticks(range(0, 170, 4), values[range(0, 170, 4), 1], rotation=45)
plt.title('2000-2017年度生成总值散点图')


#plt.show()

plt.subplot(122)


plt.xlabel('年份')
plt.ylabel('生产总值(亿元)')
plt.xticks(range(0, 70, 4), values[range(0, 70, 4), 1], rotation=45)
plt.title('2000-2017年度生成总值散点图')

plt.legend(['第一产业', '第二产业', '第三产业'])

#plt.savefig('2000-2017年度生成总值散点图2.png')
plt.show()

