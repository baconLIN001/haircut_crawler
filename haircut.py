# -*- coding: utf-8 -*-
__author__ = 'bacon'
import requests
from bs4 import BeautifulSoup
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
all_url = 'http://www.faxingzhan.com/'  ##开始的URL地址
html = requests.get(all_url,  headers=headers)  ##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
# print(html.text) ##打印出start_html (请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)
all_kinds = BeautifulSoup(html.text, 'lxml').find('div', class_='map mid').find_all('dd')
all_pres = []
for pre in all_kinds:
    a = pre.find('a')
    all_pres.append(a['href'])

all_pres.remove("https://www.faxingzhan.com/fxsj/v/")
# for pre in all_pres:
#     print(pre)

all_pages = []
srcs = []
for pre in all_pres:
    html = requests.get(pre,  headers=headers)
    # all_li_per_page = BeautifulSoup(html.text, 'lxml').find('div', class_='container mid').find_all('li')
    all_pages_per_pre = BeautifulSoup(html.text, 'lxml').find('div', class_='pages').find_all('a')
    href = all_pages_per_pre[len(all_pages_per_pre)-1]['href'].replace("-", '_')
    idx = len(href)
    for i in href[::-1]:
        if i == "_":
            idx = idx
            break
        else: idx -= 1

    num = href[idx:-5]
    new_pre = all_pages_per_pre[len(all_pages_per_pre)-1]['href'][:idx]
    print(num)
    print(new_pre)

    for i in range(1, int(num) + 1):
        new_href = new_pre + str(i) + ".html"
        all_pages.append(new_href)

for h in all_pages:
        print(h)