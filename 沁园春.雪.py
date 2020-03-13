import requests
from lxml import etree

# 确定目标网址
url = "https://so.gushiwen.org/shiwenv_202a800b9239.aspx"
# UA伪装
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 Edg/80.0.361.62"
}
# 发出HTTP请求
response = requests.get(url, headers=header)
# 获取响应数据
html = response.text
# 保存数据为HTML文件
with open("沁园春.雪.html", 'w', encoding='utf-8') as f:
    f.write(html)

# 创建解析对象
tree = etree.HTML(html)

all_html = ""

# 构建标题的xpath表达式
xpath_title = "/html/body/div/div/div/div/h1/text()"
# 进行xpath解析
list_title = tree.xpath(xpath_title)
title = ",".join(list_title)
all_html = all_html + title + "\n"

# 构建年代作者的xpath表达式
xpath_author = "/html/body/div[2]/div[1]/div[2]/div[1]/p//text()"
# 进行xpath解析
list_author = tree.xpath(xpath_author)
author = ",".join(list_author)
all_html = all_html + author + "\n"

# 构建内容的xpath表达式
xpath_content = "//div[@class='contson' and @id='contson202a800b9239' ]//text()"
# 进行xpath解析
list_content = tree.xpath(xpath_content)
content = ",".join(list_content)
all_html = all_html + content + "\n"

# 构建注释赏析的xpath表达式
xpath_other = "//div[@class='contyishang']//text()"
# 进行xpath解析
list_other = tree.xpath(xpath_other)

for other in list_other:
    if(other != '\n'):
        other = other.strip('\u3000 \n')
        all_html = all_html + other + "\n"
print(all_html)

# 保存数据为txt文件
with open("沁园春.雪.txt", 'w', encoding='utf-8') as f:
    f.write(all_html)
print('-------------------------------恭喜您，get到一首豪放的诗歌-------------------------------')



































