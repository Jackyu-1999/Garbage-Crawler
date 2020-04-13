import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(8, 8))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = True
data = np.load('国民经济核算季度数据.npz')
np.set_printoptions(threshold= np.inf)
name = data['columns']  # 提取其中的columns数组，视为数据的标签
values = data['values']
print(name)
print(values)

#  箱形图1
plt.subplot(121)
plt.title('2000-2017各产业国民生产总值箱形图')
label = ['第一产业','第二产业','第三产业']
gdp = (list(values[:,3]), list(values[:,4]),list(values[:,5]))
plt.boxplot(gdp, notch=False, labels = label, meanline=None)


#  2
plt.subplot(122)
plt.title('2000-2017各产业国民生产总值行业构成箱形图')
label = ['农业', '工业', '建筑', '批发', '交通', '餐饮', '金融', '房地产', '其它']
gdp = (list(values[:,6]),list(values[:,7]),list(values[:,8]),list(values[:,9]),list(values[:,10]),list(values[:,11]),list(values[:,12]),list(values[:,13]),list(values[:,14]),)
plt.boxplot(gdp, notch=False, labels = label, meanline=None)
plt.show()






