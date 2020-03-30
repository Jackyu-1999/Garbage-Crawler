import requests
from lxml import etree

def stripText(textList):
    str_list = ""
    for item in textList:
        item_str = item.replace('\n', "").replace('\r', "").replace('\t', "").replace('/', "").replace('-', "")
        if item_str != "":
            if str_list != "":
                str_list = str_list + "," + item_str
            else:
                str_list = item_str
    return str_list

# 代理
# proxies = {
# "https": '163.125.253.174',
# }
# UA伪装

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}

# 构建目标网址
base_url = "https://sz.sofang.com/new/area/bl"

end_page = input("请输入结束页码：")
for p in range(1, int(end_page)+1):
    page = str(p)
    url = base_url+page+"?"

    # 发送HTTP请求
    response = requests.get(url=url, headers=header)
    response.encoding = 'utf-8'
    # 获取响应数据
    html_content = response.text
    # print(html_content)
    with open('sofang'+page+'.html', 'w', encoding='utf-8')as f:
        f.write(html_content)

    parse = etree.HTMLParser(encoding='utf-8')
    tree = etree.parse('sofang'+page+'.html', parser=parse)
    print(etree.tostring(tree, encoding='utf-8').decode('utf-8'))

    item_xpath = "//div[@class='list_info clearfix']/div/div[@class='list list_free xinfang']/dl"
    item_list = tree.xpath(item_xpath)
    # print(item_list)
    all_content = []
    for item in item_list:
        if item.xpath("count(.//div[@class='list list_free xinfang']/dl/dd[@class='house_msg']/p[@class='name']/a)") == 0:
            continue
        item_dic = {}
        name_xpath = ".//div[@class='list list_free xinfang']/dl/dd[@class='house_msg']/p[@class='name']/a//text()"
        name_list = item.xpath(name_xpath)
        item_dic["name"] = stripText(name_list)
        print(item_dic["name"])

        place_xpath = ".//div[@class='list list_free xinfang']/dl/dd[@class='house_msg']/div[@class='house_info no_back']/p[@class='area clearfix']/span[@class='build_sq']"
        place_list = item.xpath(place_xpath)
        item_dic["place"] = stripText(place_list)
        print(item_dic["place"])

        price_xpath = ".//div[@class='list list_free xinfang']/dl/dd[@class='house_price']/p[@class='price margin_bottom']//text()"
        price_list = item.xpath(price_xpath)
        item_dic["price"] = stripText(price_list)
        print(item_dic["price"])

        label_xpath = ".//div[@class='list list_free xinfang']/dl/dd[@class='house_msg']/div[@class='house_info no_back']/p[@class='type clearfix']/span/text()"
        label_list = item.xpath(label_xpath)
        item_dic["label"] = stripText(label_list)
        print(item_dic["label"])

        room_xpath = ".//div[@class='list list_free xinfang']/dl/dd[@class='house_msg']/div[@class='house_info no_back']/p[@class='type clearfix']/span/text()"
        room_list = item.xpath(room_xpath)
        item_dic["room"] = stripText(room_list)
        print(item_dic["room"])

        addr_xpath = ".//div[@class='list list_free xinfang']/dl/dd[@class='house_msg']/div[@class='house_info no_back']/p[@class='area clearfix']/span[@class='address']/text()"
        addr_list = item.xpath(addr_xpath)
        item_dic["addr"] = stripText(addr_list)
        print(item_dic["addr"])

        features_xpath = ".//div[@class='list list_free xinfang']/dl/dd[@class='house_msg']/div[@class='house_info no_back']/p[@class='tag clearfix']/span//text()"
        features_list = item.xpath(features_xpath)
        item_dic["features"] = stripText(features_list)
        print(item_dic["features"])

        all_content.append(item_dic)
    # 保存为文本文件
    with open("sofang"+page+".txt", 'w', encoding='utf-8') as file:
        for item in all_content:
            file.write(str(item)+"\n")
