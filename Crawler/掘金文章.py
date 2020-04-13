import requests
from bs4 import BeautifulSoup

# 确定目标网址
url = "https://juejin.im/post/5e51febde51d4526c932b390"
# UA伪装
header = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 Edg/80.0.361.62"
}

# 发起HTTP请求
response = requests.get(url, headers=header)
# 获取响应数据
data = response.text
# 数据解析构建bs4对象
soup = BeautifulSoup(data, 'lxml')
# 网页的标题
title = soup.title.text
print(str(title))
# 文章时间
time = soup.time.attrs['datetime']
print(str(time))
# 文章标题
article_title = soup.find('h1', class_="article-title").text
print(str(article_title))
# 文章内容
article_content = soup.find('div', class_="article-content").find_all('p', limit=350)

article_p = ""
for i in article_content:
	article_p+=i.text
print(article_p)

# 保存数据为字典类型
content = {}
content['网页标题'] = title
content['发布时间'] = time
content['文章标题'] = article_title
content['文章内容'] = article_p

# 保存为txt文件
with open("ju.txt", "w", encoding="utf-8")as f:
	f.write(str(content))
