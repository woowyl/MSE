import requests
from lxml import etree
import json
import csv
import time
import random

# 获取网页源代码
def get_page(url):
    headers = {
        'USER-AGENT':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    html = response.text
    return html

# 解析网页源代码
def parse_page(html):
    html_elem = etree.HTML(html)
    links = html_elem.xpath('//div[@class="hd"]/a/@href')
    titles = html_elem.xpath('//div[@class="hd"]/a/span[1]/text()')
    infos = html_elem.xpath('//div[@class="bd"]/p[1]//text()')
    roles = [j.strip() for i,j in enumerate(infos) if i % 2 == 0]
    descritions = [j.strip() for i,j in enumerate(infos) if i % 2 != 0]
    stars = html_elem.xpath('//div[@class="bd"]/div/span[2]/text()')
    comments = html_elem.xpath('//div[@class="bd"]/div/span[4]/text()')
    data = zip(links,titles,roles,descritions,stars,comments)
    return data

# 打开文件
def openfile(fm):
    fd = None
    if fm == 'txt':
        fd = open('douban.txt','w',encoding='utf-8')
    elif fm == 'json':
        fd = open('douban.json','w',encoding='utf-8')
    elif fm == 'csv':
        fd = open('douban.csv','w',encoding='utf-8',newline='')
    return fd

# 将数据保存到文件
def save2file(fm,fd,data):
    if fm == 'txt':
        for item in data:
            fd.write('----------------------------------------\n')
            fd.write('link：' + str(item[0]) + '\n')
            fd.write('title：' + str(item[1]) + '\n')
            fd.write('role：' + str(item[2]) + '\n')
            fd.write('descrition：' + str(item[3]) + '\n')
            fd.write('star：' + str(item[4]) + '\n')
            fd.write('comment：' + str(item[5]) + '\n')
    if fm == 'json':
        temp = ('link','title','role','descrition','star','comment')
        for item in data:
            json.dump(dict(zip(temp,item)),fd,ensure_ascii=False)
    if fm == 'csv':
        writer = csv.writer(fd)
        for item in data:
            writer.writerow(item)

# 开始爬取网页
def crawl():
    url = 'https://movie.douban.com/top250?start={page}&filter='
    fm = input('请输入文件保存格式（txt、json、csv）：')
    while fm!='txt' and fm!='json' and fm!='csv':
        fm = input('输入错误，请重新输入文件保存格式（txt、json、csv）：')
    fd = openfile(fm)
    print('开始爬取')
    for page in range(0,25,25):
        print('正在爬取第 ' + str(page+1) + ' 页至第 ' + str(page+25) + ' 页......')
        html = get_page(url.format(page=str(page)))
        print(html)
        #data = parse_page(html)
        #save2file(fm,fd,data)
        time.sleep(random.random())
    fd.close()
    print('结束爬取')


# 另一个爬虫
def crawl2():
    url = "https://movie.douban.com/subject/10477598/comments"
    html = get_page(url)
    print(html)

if __name__ == '__main__':
    crawl2()