# 拉勾是一个典型的ajax异步加载的网站，我们需要找到它的真实url地址
# 在xhr接口那进行分析，真实的url地址在打开preview或response的时候会显示职位的信息
import requests
import csv
import time

# 动态接口
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

# 向展示信息的页面发出请求，拿到cookie,并返回
def get_cookie():
    cookie = requests.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }, allow_redirects=False).cookies
    return cookie

# 构造请求头，接收用户输入的页数和关键字作为参数传入函数内部，发起post请求，提取json中的招聘数据保存至变量html，再传给savedata函数
def put_into(page, kd):
    headers = {
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    json = {
        'first': 'true',
        'pn': str(page),
        'kd': str(kd)
    }
    response = requests.post(url=url, headers=headers, data=json, cookies=get_cookie())
    response.encoding = response.apparent_encoding
    html = response.json()['content']['positionResult']['result']
    savedata(html, kd)

# 数据持久化
def savedata(html,kd):
    f = open(kd + '.csv', mode="a+", newline='', encoding='utf-8-sig')
    csv_write = csv.writer(f)
    csv_write.writerow(['职位名称', '公司名称', '公司规模', '薪资待遇', '工作经验', '是否全职', '学历要求', '公司福利', '发布时间'])
    for i in range(len(html)):
        positionName = html[i]['positionName']  # 职位名称
        companyFullName = html[i]['companyFullName']  # 公司名称
        companySize = html[i]['companySize']  # 公司规模
        salary = html[i]['salary']  # 薪资待遇
        workYear = html[i]['workYear']  # 工作经验
        jobNature = html[i]['jobNature']  # 是否全职
        education = html[i]['education']  # 学历要求
        positionAdvantage = html[i]['positionAdvantage']  # 公司福利
        lastLogin = html[i]['lastLogin']  # 发布时间
        # print(positionName,companyFullName,companySize,salary,workYear,jobNature,education,positionAdvantage,lastLogin)
        csv_write.writerow([positionName, companyFullName, companySize, salary, workYear, jobNature, education, positionAdvantage, lastLogin])
    f.close()

if __name__ == '__main__':
    kd = str(input('请输入您想爬取的职业关键词：'))
    for page in range(2, 31):
        put_into(page, kd)
        print('恭喜您,第'+str(page-1)+'页爬取成功!')
        time.sleep(2)