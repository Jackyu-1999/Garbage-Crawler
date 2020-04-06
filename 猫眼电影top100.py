import requests
import parsel
import re
import csv
import time
m = open('猫眼100.csv', mode="a", encoding="gb18030")
csv_write = csv.writer(m)
csv_write.writerow(['电影名称', '图片', '主演', '评分', '上映时间'])

for page in range(10):
    url = "https://maoyan.com/board/4?offset=" + str(page*10)
    cookie_str = '__mta=146692363.1578709708210.1578801335843.1578805309861.28; uuid_n_v=v1; uuid=0B422620341A11EAB15E198FC0D9AFBF00847B9686D84054BD9C0BD2A9891DA4; _lxsdk_cuid=16f926e6c59c8-0cf9a49f43eaa4-2393f61-100200-16f926e6c59c8; _lxsdk=0B422620341A11EAB15E198FC0D9AFBF00847B9686D84054BD9C0BD2A9891DA4; mojo-uuid=867823097861e30504e3d87083711579; _csrf=e0ab6c247f6b08aa205b6bd7bfe2e90e8e3f30c0b44e049758bf593690ffd473; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1578709730,1578759108,1578796254,1578796772; mojo-session-id={"id":"492639051b5947dc76ddd544ce7bcf06","time":1578804238464}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1578805309; _lxsdk_s=16f98210326-c23-cd-328%7C%7C3'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Host": "maoyan.com",
        "Origin": "https://maoyan.com",
        "Referer": "https://maoyan.com/board/4?offset="+str(page*10),
        "Cookie": cookie_str
    }
    json = {
        "offset": str(page*10)
    }
    response = requests.get(url, headers=headers, data=json)
    response.encoding = response.apparent_encoding
    html = response.text
    #print(html)

    selector = parsel.Selector(html)
    # 编写xpath规则，/表示从网页最开始的地方提取节点，//是提取任意节点,[]指定选择属性

    dds = selector.xpath('//dd/a/img[2]')
    stars = selector.xpath('//p[@class="star"]/text()')
    dates = selector.xpath('//p[@class="releasetime"]/text()')
    scores1 = selector.xpath('//p[@class="score"]/i[@class="integer"]')
    scores2 = selector.xpath('//p[@class="score"]/i[@class="fraction"]')

    for i in range(len(dds.getall())):
        result = re.findall('data-src=".*?"', dds.getall()[i])
        image = result[0].split('=')[-1]
        image = eval(str(image))
        image = image.split('@')[0]
        result1 = re.findall('alt=".*?"', dds.getall()[i])
        name = result1[0].split('=')[-1]
        name = eval(str(name))
        star = (stars.getall()[i].split('\\n')[0]).split('：')[-1].strip()
        date = (dates.getall()[i]).split('：')[-1].strip()

        score1_result = re.findall('\d+', scores1.getall()[i])
        score2_result = re.findall('\d+', scores2.getall()[i])
        score = str(score1_result[0]) + '.' + str(score2_result[0])
        csv_write.writerow([str(name), str(image), str(star), str(score), str(date)])
        print(name.ljust(0),'\t',image.ljust(40),'\t',star,'\t',score,'\t'*6,date.rjust(10))
    print('第'+str(page)+'页采集完毕！')
    time.sleep(2)