from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import os
import time


ua = UserAgent()
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://www.wnacg.com'
}


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


# 文件下载器
def down_load(file_url, file_full_name, now_count, all_count, headers):
    if os.path.exists(file_full_name):
        return
    # 开始下载图片
    response = requests.get(file_url, headers=headers, stream=True)
    chunk_size = 1024  # 单次请求最大值
    content_size = int(response.headers.get('content-length'))  # 文件总大小
    data_count = 0  # 当前已传输的大小
    with open(file_full_name, "wb") as file:
        for data in response.iter_content(chunk_size=chunk_size):
            file.write(data)
            done_block = int((data_count / content_size) * 50)
            data_count = data_count + len(data)
            now_jd = (data_count / content_size) * 100
            print("\r %s：[%s%s] %d%% %d/%d" % ('***'+file_full_name[-10:], done_block *
                                               '█', ' ' * (50 - 1 - done_block), now_jd, now_count, all_count), end=" ")


def all_down(url, path):
    r = requests.get(url).text
    soup = BeautifulSoup(r, "lxml")
    start_img = soup.select("#bodywrap  li:nth-child(1) a")[0]["href"]
    title = soup.select("#bodywrap > h2")[0].get_text()
    path = path+"/"+title
    mkdir(path)
    start = "https://www.wnacg.com" + start_img
    r = requests.get(start).text
    soup = BeautifulSoup(r, "lxml")
    first_img = "https:" + soup.select("#picarea")[0]["src"]
    startNum = int(first_img.rsplit("/", 1)[1].split(".", 1)[0])
    total = soup.select("span.newpagelabel")[0].get_text().split("/", 1)[-1]
    typeName = first_img.rsplit("/", 1)[1].split(".", 1)[1]
    lens = len(total)
    total = int(total)
    for i in range(startNum, total + 1):
        time.sleep(1)
        down_load(first_img.rsplit('/', 1)[0] + "/" + f"{i:0>{lens}}" + "." +
                  typeName, path + "/" + f"{i:0>{lens}}" + "." + typeName, i, total, headers)


url = "https://www.wnacg.com/photos-index-aid-83594.html"
all_down(url, "./Tmp")
