import requests
import uuid
from lxml import etree
import pymysql

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

header = {
    "Cookie": "HWWAFSESID=056a5768aa5fba4214; HWWAFSESTIME=1585625690764; ASP.NET_SessionId=4vfwttngyeyoaf452b41wr5p",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

all_content = []

# 构造url
base_url = "http://csga.changsha.gov.cn/jjzd/csjj_index/topic_4169_"
end_page = input("请输入结束页: ")
for p in range(1, int(end_page)+1):
    url = base_url+str(p)+".shtml"
    # 发出HTTP请求
    response = requests.get(url=url, headers=header)
    response.encoding = response.apparent_encoding
    # 获取响应数据
    html_content = response.text
    # print(html_content)
    with open('../html/交通违法.html', 'w', encoding='utf-8')as f:
        f.write(html_content)

    tree = etree.HTML(html_content)
    item_xpath = "//div[@id='newsdata']/div[@class='info_list_top']/a[@class='morePointer']/@href"
    item_list = tree.xpath(item_xpath)
    # print(item_list)

    for item in item_list:
        detail_url = item
        response_detail = requests.get(url=detail_url, headers=header)
        response_detail.encoding = response_detail.apparent_encoding
        detail_content = response_detail.text
        # print(detail_content)

        detail_tree = etree.HTML(detail_content)
        count = detail_tree.xpath("count(//table/tbody/tr)")
        # print(count)

        for i in range(2, int(count)):
            i = str(i)
            item_detail = {}

            item_detail["id"] = str(uuid.uuid1())

            traffice_time = stripText(detail_tree.xpath("//table/tbody/tr["+i+"]/td[2]//text()"))
            print(traffice_time)
            item_detail["traffice_time"] = traffice_time

            addr = stripText(detail_tree.xpath("//table/tbody/tr[" + i + "]/td[3]//text()"))
            print(addr)
            item_detail["addr"] = addr

            car_code = stripText(detail_tree.xpath("//table/tbody/tr[" + i + "]/td[4]//text()"))
            print(car_code)
            item_detail["car_code"] = car_code

            car_type = stripText(detail_tree.xpath("//table/tbody/tr[" + i + "]/td[5]//text()"))
            print(car_type)
            item_detail["car_type"] = car_type

            behavior = stripText(detail_tree.xpath("//table/tbody/tr[" + i + "]/td[6]//text()"))
            print(behavior)
            item_detail["behavior"] = behavior

            result = stripText(detail_tree.xpath("//table/tbody/tr[" + i + "]/td[7]//text()"))
            print(result)
            item_detail["result"] = result

            all_content.append(item_detail)
print(all_content)

# mysql数据存储

def insertDicData(table, all_content):
    # table = "traffice"
    data = all_content[0]
    cols = ",".join('`{}`'.format(k) for k in data.keys())
    print(cols)
    cols_value = ",".join('%({})s'.format(k) for k in data.keys())
    print(cols_value)

    sql = "insert into " + table + "(%s) values(%s)"
    res_sql = sql % (cols, cols_value)
    print(res_sql)
    cursor.executemany(res_sql, all_content)
    db.commit()

db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123", db="trafficeDB")
cursor = db.cursor()

insertDicData("traffice", all_content)




