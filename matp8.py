import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
plt.figure(figsize=(9, 9))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = True
# 饼状图1
plt.subplot(221)
plt.title("2000年第一季度国民生产总值饼状图")
labels = ['第一产业', '第二产业', '第三产业']
X = [89, 448, 463]
plt.pie(X, labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）

#  2
plt.subplot(222)
plt.title("2017年第一季度国民生产总值饼状图")
labels = ['第一产业', '第二产业', '第三产业']
X = [48, 387, 565]
plt.pie(X, labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）

# 3
plt.subplot(223)
plt.title("2000年第一季度国民生产总值行业构成饼状图")
labels = ['农业', '工业', '建筑', '批发', '交通', '餐饮', '金融', '房地产', '其它']
X = [91, 413, 36, 98, 65, 27, 58, 44, 168]
plt.pie(X, labels=labels, autopct='%1.2f%%')
# 4
plt.subplot(224)
plt.title("2017年第一季度国民生产总值行业构成饼状图")
labels = ['农业', '工业', '建筑', '批发', '交通', '餐饮', '金融', '房地产', '其它']
X = [50, 343, 46, 98, 45, 19, 95, 69, 235]
plt.pie(X, labels=labels, autopct='%1.2f%%')







plt.show()

