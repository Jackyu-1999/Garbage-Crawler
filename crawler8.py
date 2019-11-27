import requests
from multiprocessing import Pool

#  爬电影

def temp(i):
    # 某个文件的url
    url = "https://leshi.cdn-zuyida.com/20180127/mO2ad0Th/800kb/hls/KwDM28077000.ts" % i
    # 模拟浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0"
    }
    # 使用 requets.get方法返回当前url的信息
    r = requests.get(url, headers=headers)
    # 在控制台打印返回的信息
    print(r)
    with open('{}'.format(url[-10:]), 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    pool = Pool(30)
    for i in range(1999):
        pool.apply_async(temp, (i,))

    pool.close()
    pool.join()