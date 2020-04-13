import re
import urllib.request


# 定义一个爬取网络小说的函数
def getNovelContent():
    html = urllib.request.urlopen("https://www.luoxia.com/shujian/").read()  # 读取网页源代码
    html = html.decode("utf-8")  # 转成该网址的格式
    # 参考
    reg = r'<a target="_blank" title="(.*?)" href="(.*?)">.*?</a>'  # 正则匹配
    reg = re.compile(reg)  # 可添加可不添加，增加效率
    urls = re.findall(reg, html)
    for url in urls:
        #print(url)
        chapter_title = url[0]  # 章节的名字
        chapter_url = url[1]  # 章节的超链接

        print(chapter_title)
        # print(chapter_url)
        # 如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误
        # 主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WiW64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}

        # Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0

        chapter_url = urllib.request.Request(url=chapter_url, headers=headers)

        chapter_html = urllib.request.urlopen(chapter_url).read()  # 正文内容源代码
        chapter_html = chapter_html.decode("utf-8")
        chapter_reg = r'<p>(.*?)</p>'
        # print(chapter_html)
        chapter_reg = re.compile(chapter_reg, re.S)
        url2 = re.findall(chapter_reg, chapter_html)
        for url1 in url2:
            print(url1)
            f = open('{}.txt'.format(chapter_title), 'w')      # 保存到文本
            f.write(url1)  # 可能是版权原因，无法将内容写入
getNovelContent()










