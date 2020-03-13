import requests
from bs4 import BeautifulSoup

# 确定目标网址
url = "https://www.proginn.com/search"
# UA伪装
header = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36 Edg/80.0.361.62"
}
# 以循环的方式发送HTTP请求
word = input("请输入搜索关键字: ")
end_page = input("请输入结束页面号码: ")
for page in range(1, int(end_page)+1):
	param ={
		"keyword": word,
		"page": str(page)

	}
	response = requests.get(url=url, headers=header, params=param)
	# 获取响应数据
	html = response.text
	# 数据解析，构建bs4对象
	soup = BeautifulSoup(html, 'lxml')
	# 用户名标签列表
	name = soup.select('p.user-name')
	# 职位标签列表
	title = soup.select('div.title > a.info')
	# 技能
	skill = soup.select('p.desc-item:nth-child(2) > span')
	# 作品
	work = soup.select('p.desc-item:nth-child(3) > span')
	# 工作地点和时间
	father = soup.select('div.work-time')
	content = []
	for i in range(len(name)):
		# 用户名
		cName = name[i].text
		# 职位
		cTitle = title[i].attrs['title']
		# 技能
		cSkills = skill[i].text
		# 作品
		cWorks = work[i].text
		# 工作地点
		cAddres = father[i].div.text
		# 工作时间
		for t in father[i].div.next_siblings:
			cTime = t.text

		c ={
			"name": cName,
			"position": cTitle,
			"skills": cSkills,
			"works": cWorks,
			"address": cAddres,
			"time": cTime
		}
		content.append(c)
	for value in content:
		with open("程序员客栈.txt", "a", encoding="utf-8")as f:
			f.write(str(value)+"\n")
			