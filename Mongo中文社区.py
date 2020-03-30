import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# 确定目标网址的基础url
base_url = "https://mongoing.com/page/"

# 伪装
header = {
    'Host': 'mongoing.com',
    'Referer': 'https://mongoing.com/',
    'TE': 'Trailers',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    'X-Requested-With': 'XMLHttpRequest'
}
end_page = input("请输入你要加载的页数:")
content = []

# 循环发送HTTP请求
for page in range(1, int(end_page)+1):
    # 拼接成完整的url
    url = base_url+str(page)
    response = requests.get(url, headers=header)
    # 获取网站的响应数据
    html = response.text
    # 数据解析
    soup = BeautifulSoup(html, 'lxml')
    # 获取article标签
    article = soup.select('div.content article.excerpt-text')
    # 存储链接和页码
    url_data = {
        'url': url,
        'page': page
    }
    content.append(url_data)
    # 组合数据
    for i in range(len(article)):
        # 标题
        title = article[i].h2.text
        # 时间
        time = article[i].time.text
        # 作者
        author = article[i].find('span', class_='author').text
        # 评论
        comment = article[i].find('a', class_='pc').text
        # 摘要
        note = article[i].find('p', class_='note').text.replace('\r', '').replace('\n', '')
        c = {
            'id': (i+1),
            'title': title,
            'time': time,
            'author': author,
            'comment': comment,
            'note': note
        }
        content.append(c)
print(str(content))
# 数据存储
# 1.连接数据库
client = MongoClient('localhost', 27017)
# 创建数据库
db = client.mongo1
# 创建集合
column = db.infos
# 数据存储到数据库
# 插入数据
# column.insert_many(content)

# 查询
# 查询一条数据
# find_one = column.find_one({'page': 1})
# 查询所有数据
# find_all = column.find()
# for data in find_all:
#     print(data)
# 查询带条件的所有数据
# find_all = column.find({'id': 1})
# 查询id>7 $lt 小于 $gt 大于
# find_all = column.find({
#     'id': {'$gt': 7}
# })
# 多条件查询 $and $or
# find_all = column.find({
#     '$and': [
#         {'id': {'$gt': 7}},
#         {'time': {'2020-01-22'}}
#     ]
# })
# print(type(find_all))
# for data in find_all:
#     print(data)

# 更新
# 更新一条数据
# update_one = column.update_one(
#     {'page': 1},
#     {'$set': {'url': 'https://mongoing.com/page/1-update'}}
# )
# data1_result = column.find_one({'page': 1})
# # print(data1_result)
# # 更新多条数据
update_many = column.update_many(
    {'id': 1},
    {'$set': {'time': '莫晓得'}}
)
data2_result = column.find({'id': 1})
for data in data2_result:
    print(data)

# # 删除
# # 删除单条记录
# # column.delete_one({'id': 1})
# 删除多条记录
column.delete_many({'id': 3})
all_data = column.find()
for data in all_data:
    print(data)





































