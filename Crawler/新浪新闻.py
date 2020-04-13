import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

url ="https://news.sina.cn/global/szzx/2019-12-01/detail-iihnzhfz2926782.d.html"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
response = requests.get(url, headers=header)

html = response.content.decode('utf-8')

soup = BeautifulSoup(html, 'lxml')
# 标题
title = soup.h1.text

# 时间和来源
time = soup.find('time', class_="art_time").text

# 文章内容
article = soup.find('section', class_='art_pic_card art_content').text

# 组合数据
data = {
    'title': title,
    'time': time,
    'article': article
}
# 使用mongodb数据库存储
# 1.连接数据库
# 无参数
# client = MongoClient()
# 有参数
# client = MongoClient('localhost', 27017)
# url方式
client = MongoClient('mongodb://localhost:27017/')
# 创建或访问数据库
# 1.以'.'的形式
# db=client.test_database
# 2.以数据字典的形式
db = client['new_database']
# 创建或访问数据集合
# 1.以'.'的形式
# column=db.article
# 2.以数据字典的形式
column = db['article']
#  插入数据
result = column.insert_one(data)
print(result)










