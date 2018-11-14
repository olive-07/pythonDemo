import os
import time
from multiprocessing import Pool
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

import dbtest

__imageList = "imageList"
__titleList = "titleList"
__linkList = "linkList"
__http = "http:"


def get_html(url, headers):
    # 获取网页
    html = requests.get(url=url, headers=headers).text.encode("utf-8")
    return html


def get_content(html):
    # 获取内容
    Soup = BeautifulSoup(html, "lxml")
    p_div = Soup.select('div[class="head"]')
    image_list = []
    title_list = []
    link_list = []
    content = {}
    for p in p_div:
        div = p.find_all("div", class_="Q-tpList")
        for i in div:
            a_div = i.div
            src = a_div.a.img['src']
            image_list.append(src)

            a = a_div.div.em.a
            title = a.get_text()
            title_list.append(title)

            link = a['href']
            link_list.append(link)
        break
    content[__imageList] = image_list
    content[__titleList] = title_list
    content[__linkList] = link_list
    return content


def save_news(content):
    title_list = content[__titleList]
    link_list = content[__linkList]
    image_list = content[__imageList]
    # 写入DB
    db = dbtest.mysqlDB()
    for i in range(0, len(title_list)):
        db.insertNews(title_list[i], link_list[i], __http + image_list[i])
    db.close()

    # 写入文件
    with open("news.txt", "a", encoding="utf-8") as fo:
        fo.write('\n')
        for size in range(0, len(title_list)):
            fo.write("标题：" + title_list[size] + " 链接：" + link_list[size] + " 图片地址：" + __http + image_list[size] + '\n')
        fo.close()

    # 下载图片
    download_image(image_list, processes=10)


def download_image(image_list, processes=10):
    """ 并发下载所有图片 """
    start_time = time.time()
    pool = Pool(processes)
    for size in range(0, len(image_list)):
        pool.apply_async(download, (__http + image_list[size], str(start_time) + str(size),))

    pool.close()
    pool.join()
    end_time = time.time()
    print('下载完毕,用时:%s秒' % (end_time - start_time))


def setup_download_dir(directory):
    """ 设置文件夹，文件夹名为传入的 directory 参数，若不存在会自动创建 """
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except Exception:
            pass


def download(img_url, img_name):
    # 如果文件已经存在，放弃下载
    directory = "temp\\"
    setup_download_dir(directory)
    img_path = directory + img_name + ".jpg"
    # 如果文件已经存在，放弃下载
    # if os.path.exists(img_path):
    #     print('exists:', img_path)
    #     return
    try:
        f = open(img_path, "wb")
        f.write(urlopen(img_url).read())
        f.close()
    except Exception:
        print(img_url + " error")


def grab(second):
    while True:
        print('开始抓取:%s' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        start_time = time.time()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"}
        url = "http://news.qq.com/"
        html = get_html(url, headers)
        content = get_content(html)
        save_news(content)
        end_time = time.time()
        print('抓取完毕,用时:%s秒' % (end_time - start_time))
        time.sleep(second)


def main():
    grab(60)


if __name__ == "__main__":
    main()
