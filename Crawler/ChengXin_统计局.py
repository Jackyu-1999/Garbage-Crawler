import requests
from lxml import etree
import csv
import pandas as pd

def stripText(textList):
    str_list = ""
    for item in textList:
        item_str = item.strip().replace('\n', "").replace('\r', "").replace('\t', "").replace('/', "").replace('-', "")
        if item_str != "":
            if str_list != "":
                str_list = str_list + "" + item_str
            else:
                str_list = item_str
    return str_list

# UA伪装
header = {
    "Cookie": "AD_RS_COOKIE=20080918",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 Edg/80.0.361.62"
}

# 构建目标网址
# url = "http://www.stats.gov.cn/tjfw/sxqygs/gsxx/index.html"
base_url = "http://www.stats.gov.cn/tjfw/sxqygs/gsxx/index"
end_page = input("请输入结束页: ")

all_content = []
for p in range(1, int(end_page)+1):
    if p == 1:
        url = base_url + ".html"
    else:
        page = str(p)
        url = base_url + "_"+page+".html"
    # 发出HTTP请求
    response = requests.get(url, headers=header)
    response.encoding = 'utf-8'
    # 获取响应数据
    html = response.text
    # 保存数据
    with open("../html/诚信"+str(p)+".html", 'w', encoding='utf-8')as f:
        f.write(html)

    tree = etree.HTML(html)
    item_xpath = "//ul[@class='center_list_contlist']/li/a/@href"
    item_list = tree.xpath(item_xpath)
    print(item_list)

    for item in item_list:
        item_dic = {}
        detail_url = "http://www.stats.gov.cn/tjfw/sxqygs/gsxx"+item
        # 再次发出请求
        detail_response = requests.get(url=detail_url, headers=header)
        detail_response.encoding = 'utf-8'
        detail_content = detail_response.text
        detail_tree = etree.HTML(detail_content)

        name = stripText(detail_tree.xpath("//table[@class='MsoNormalTable']/tbody/tr[1]/td[2]/p[@class='MsoNormal']//text()"))
        print(name)
        item_dic["name"] = name

        addr = stripText(detail_tree.xpath("//table[@class='MsoNormalTable']/tbody/tr[2]/td[2]/p[@class='MsoNormal']//text()"))
        print(addr)
        item_dic["addr"] = addr

        code1 = stripText(detail_tree.xpath("//table[@class='MsoNormalTable']/tbody/tr[3]/td[2]/p[@class='MsoNormal']//text()"))
        print(code1)
        item_dic["code1"] = code1+'\t'

        person = stripText(detail_tree.xpath("//table[@class='MsoNormalTable']/tbody/tr[5]/td[2]/p[@class='MsoNormal']//text()"))
        print(person)
        item_dic["person"] = person

        code2 = stripText(detail_tree.xpath("//table[@class='MsoNormalTable']/tbody/tr[6]/td[2]/p[@class='MsoNormal']//text()"))
        print(code2)
        item_dic["code2"] = code2

        thing = stripText(detail_tree.xpath("//table[@class='MsoNormalTable']/tbody/tr[7]/td[2]/p[@class='MsoNormal']//text()"))
        print(thing)
        item_dic["thing"] = thing

        deal1 = stripText(detail_tree.xpath("//table[@class='MsoNormalTable']/tbody/tr[8]/td[2]/p[@class='MsoNormal']//text()"))
        print(deal1)
        item_dic["deal1"] = deal1

        deal2 = stripText(detail_tree.xpath("//table[@class='MsoNormalTable']/tbody/tr[9]/td[2]/p[@class='MsoNormal']//text()"))
        print(deal2)
        item_dic["deal2"] = deal2

        deal_gist = stripText(detail_tree.xpath("//table[@class='MsoNormalTable']/tbody/tr[10]/td[2]/p[@class='MsoNormal']//text()"))
        print(deal_gist)
        item_dic["deal_gist"] = deal_gist

        deal_matter = stripText(detail_tree.xpath("//table[@class='MsoNormalTable']/tbody/tr[11]/td[2]/p[@class='MsoNormal']//text()"))
        print(deal_matter)
        item_dic["deal_matter"] = deal_matter

        deal_office = stripText(detail_tree.xpath("//table[@class='MsoNormalTable']/tbody/tr[12]/td[2]/p[@class='MsoNormal']//text()"))
        print(deal_office)
        item_dic["deal_office"] = deal_office

        deal_date = stripText(detail_tree.xpath("//table[@class='MsoNormalTable']/tbody/tr[13]/td[2]/p[@class='MsoNormal']//text()"))
        print(deal_date)
        item_dic["deal_date"] = deal_date

        public = stripText(detail_tree.xpath("//table[@class='MsoNormalTable']/tbody/tr[14]/td[2]/p[@class='MsoNormal']//text()"))
        print(public)
        item_dic["public"] = public

        state = stripText(detail_tree.xpath("//table[@class='MsoNormalTable']/tbody/tr[15]/td[2]/p[@class='MsoNormal']//text()"))
        print(state)
        item_dic["state"] = state

        all_content.append(item_dic)

# with open("../data/国家统计局.csv", 'w', newline='')as fp:
#     for item in all_content:
#         writer = csv.writer(fp)
#         writer.writerow(item.values())

# with open("../data/诚信.csv", 'r')as csv_file:
#     lines = csv.reader(csv_file)
#     for line in lines:
#          print(line)

# 使用pandas存储csv文件
df = pd.DataFrame(data=all_content, columns=['name', 'addr', 'code1', 'person', 'code2', 'thing', 'deal1', 'deal2', 'deal_gist', 'deal_matter', 'deal_office', 'deal_date', 'public', 'state'])
df.to_csv("../data/国家统计局.csv", encoding='gbk')
print(df)

# # pandas读文件
df2 = pd.read_csv("../data/诚信.csv", encoding='gbk')
print(df2.head(5))














        















