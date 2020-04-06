import requests

url = "https://accounts.douban.com/j/mobile/login/basic"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
data = {
    'ck': '',
    'name': '18773909514',
    'password': 'yzp917808',
    'remember': 'false',
    'ticket': ''
}
# 发出http请求
session = requests.session()
response_login = session.post(url=url, headers=headers, data=data)
response_login.encoding = response_login.apparent_encoding
# 获取响应数据
html = response_login.text
print(response_login.status_code)
# 进行持久化
with open("../html/豆瓣登录.html", 'w', encoding='utf-8')as f:
    f.write(html)

url = "https://www.douban.com/"
# 发出http请求
response_home = session.get(url=url, headers=headers)
response_home.encoding = response_home.apparent_encoding
# 获取响应数据
html_data = response_home.text
print(response_home.status_code)
# 进行持久化
with open("../html/豆瓣首页.html", 'w', encoding='utf-8')as file:
    file.write(html_data)