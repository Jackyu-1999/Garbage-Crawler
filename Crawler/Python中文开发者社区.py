import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

base_url = "https://www.pythontab.com/html/pythonjichu/"

header = {
    "Host": "www.pythontab.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

end_page = input("请输入你要加载的页码: ")
content = []
for page in range(1, int(end_page)+1):
    page = str(page)
    url = base_url + str(page) + '.html'
    response = requests.get(url, headers=header)
    # 获取网站的响应数据
    html = response.text
    # print(str(html))
    # 构建bs4解析对象
    soup = BeautifulSoup(html, 'lxml')
    textlist = soup.find_all('ul', class_='list lh24 f14')
    # for循环找到所有h2标签
    for h2 in textlist:
        txtlist1 = h2.find_all('h2')
        # for循环嵌套再遍历找出需要的标题内容
        for i in txtlist1:
            # 字符串转列表
            txtstr = i.string
            list3 = txtstr.split(".")
            # print(list3)
            b = {
                'url': url,
                'page': page,
                'title': list3
            }
            content.append(b)
    # for循环找到所有p标签
    for p in textlist:
        txtlist2 = p.find_all('p')
        # for循环嵌套再遍历找出需要的摘要内容
        for i in txtlist2:
            txtstr = i.string
            # 字符串转列表
            list4 = txtstr.split(".")
            # print(list4)
            c = {
                'note': list4
            }
            content.append(c)
print(str(content))

# 数据存储
# 1.连接数据库
client = MongoClient('localhost', 27017)
# 创建数据库
db = client.mongo2
# 创建集合
column = db.infos
# 数据存储到数据库
# 插入数据
column.insert_many(content)

# 查询
# 查询一条数据
# find_one = column.find_one({'page': 2})
# 查询所有数据
find_all = column.find()
for data in find_all:
    print(data)

# 更新
# 更新一条数据
# update_one = column.update_one(
#      {'page': 2},
#      {'$set': {'url': 'https://www.baidu.com'}}
# )
# data1_result = column.find_one({'page': 2})
# print(data1_result)

# 删除
#  删除单条记录
column.delete_one({'page': 2})












