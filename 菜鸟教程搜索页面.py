import requests
from bs4 import BeautifulSoup

# 确定目标网址
url = "https://www.runoob.com/"
# UA伪装
header = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 Edg/80.0.361.62"
}
# 以循环的方式发送HTTP请求
word = input("请输入搜索关键字: ")
end_page = input("请输入页码：")
for page in range(1, int(end_page)):
    param ={
        "s": word,
        "page": end_page
    }
    response = requests.get(url, headers=header, params=param)
    # 获取响应数据
    html = response.content.decode('utf-8')
    # 数据解析，构建bs4对象
    soup = BeautifulSoup(html, 'lxml')
    # 找到div下所有class为archive-list-item的标签
    textlist = soup.find_all('div', class_='archive-list-item')
    # for循环找到所有p标签
    for content in textlist:
        txtlist = content.find_all('p')
        # for循环嵌套再遍历找出需要的文本内容,并转换为字符串类型
        for i in txtlist:
            txtstr = i.string
            print(txtstr)
            # 保存文件为txt
            with open("菜鸟教程.txt", 'a', encoding='utf-8')as f:
                f.write(str(txtstr))
