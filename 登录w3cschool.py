import requests

url = "https://www.w3cschool.cn/index/checkHeader"

headers = {
    "Cookie": "istopad=1; ypre_saltkey=pD311swg; PHPSESSID=dtctfn7ilc38bn1ibj3ocr182p; ypre_tn=0; ypre_utype=1; ypre_fcode=headeruser; ypre_auth=0322YUtoQDtYGvjaz3Cr5KQiWjUcMKslblBZoywXEy5Zq8aiVMApR2Jk%2BN8U40UPpOCYMvf%2BRRi9aWPnBy9vmcSqAQ%2B2; ypre_sauth=6710PPf%2B5CN%2BqFE94CV8%2BK8pEVcgjXoHx4aKCexzEtLllWmQ%2BdqMbkM9UANKkF4OjaofFuxBKJHRNjmNoUS6DhVczxhP; ypre_uid=1867365",
    "Host": "www.w3cschool.cn",
    "Origin": "https://www.w3cschool.cn",
    "Referer": "https://www.w3cschool.cn/vip",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
}
params = {
    'headerType': '0',
    '_hash': 'pD311swg'
}


session = requests.session()
response = session.get(url, headers=headers, params=params)
response.encoding = response.apparent_encoding
html = response.text
print(response.status_code)
# 进行持久化
with open("../html/w3c登录.html", 'w', encoding='utf-8')as f:
    f.write(html)

url = "https://www.w3cschool.cn/vip"

response_home = session.get(url, headers=headers)
response_home.encoding = response_home.apparent_encoding
html_data = response_home.text
print(response_home.status_code)
# 进行持久化
with open("../html/w3c首页.html", 'w', encoding='utf-8')as f:
    f.write(html_data)