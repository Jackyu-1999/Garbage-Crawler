import requests
from lxml import etree
import time
import threading,psutil,os
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
}

def stripText(textList):
    str_list = ""
    for item in textList:
        item_str = item.replace('\n', "").replace('\r', "").replace('\t', "").replace('-', "").replace(' ', "")
        if item_str != "":
            if str_list != "":
                str_list = str_list + "," + item_str
            else:
                str_list = item_str
    return str_list


def downMP4(item):
    start_time = time.time()
    video_page_url = "http://699pic.com"+item
    video_page_response = requests.get(url=video_page_url, headers=header)
    video_page_content = video_page_response.text
    print(video_page_response.status_code)

    tree_video = etree.HTML(video_page_content)
    xpath_video_src = "//div/video/source/@src"
    video_url = "http:" + stripText(tree_video.xpath(xpath_video_src))
    # print(video_url)

    xpath_video_name = "//div[@class='video-view fl']/div[@class='video-view-title clearfix']/h1/text()"
    video_name = stripText(tree_video.xpath(xpath_video_name))

    print(video_url,video_name,'开始下载...')
    thread = threading.current_thread()
    process = psutil.Process(os.getpid())
    print("当前线程名称:%s,ID:%s,进程名称%s:ID:%s"
          % (thread.getName(), thread.ident, process.pid, process.name()))

    video_response = requests.get(url=video_url, headers=header)
    video_content = video_response.content
    print(video_response.status_code)

    with open(video_name+".mp4", 'wb')as f:
        f.write(video_content)

    print(video_url, video_name, '下载完成...')
    end_time = time.time() - start_time
    return video_name+".mp4 用时"+str(end_time)+"秒"

def clll_back(res):
    re = res.result()
    print(re)

def parsePage():
    url = "http://699pic.com/media/video-1142643.html"
    response = requests.get(url=url, headers=header)
    html = response.text
    print(response.status_code)
    with open("../html/hero.html", 'w', encoding='utf-8')as f:
        f.write(html)
    tree = etree.HTML(html)
    xpath_video_page = "//div[@class='search-video-wrap']/div[@class='video-list clearfix']/ul/li/a[1]/@href"
    item_list = tree.xpath(xpath_video_page)[0:3]
    start_time = time.time()
    # for item in item_list:
    #     result = downMP4(item)
    #     print(result)
   # 多进程
    # executor = TProcessPoolExecutor(max_workers=4)
    # for item in item_list:
    #     executor.submit(downMP4,item).add_done_callback(clll_back)
    # executor.shutdown(True)
    # 多线程
    with ThreadPoolExecutor(max_workers=4)as executor:
        futures = executor.map(downMP4, item_list)
        for future in futures:
            print(future)

    print("下载总时间:%s 秒 "% (time.time() - start_time))

if __name__=='__main__':
    parsePage()