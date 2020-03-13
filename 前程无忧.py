import requests
import re

# 获取用户输入
word = input("请输入您要搜索的职位关键字：")
# 确定目标网址
url = "https://search.51job.com/list/000000,000000,0000,00,9,99,"+word+",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

# 获取响应数据并解码
response = requests.get(url)
data = response.content.decode("GBK")

# 设置正则表达式
pattern = r'class="t1 ".*?<a target="_blank" title="(.*?)" href="(.*?)">.*?<span class="t2"><a target="_blank" title="(.*?) href="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>.*?'
content = re.findall(pattern, data, re.S)
print(content)

# 写入文本文件
with open("51job1.txt", "w", encoding="GBK") as f:
    f.write(str(content))

print('数据已保存！')







