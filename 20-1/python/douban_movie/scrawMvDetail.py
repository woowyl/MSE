# coding: utf-8
import requests 
import json
from lxml import etree
import csv
import time 
import random
from cons import headerChange
from bs4 import BeautifulSoup
import bs4
import os.path
from fake_useragent import UserAgent  
from requests.adapters import HTTPAdapter

ua = UserAgent(use_cache_server=False) 
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))

APIEND = 2
#每次读取的长度
STEP = 1
ipList = []
def get_ip_list():
    #国内高匿代理ip网站
    url = 'http://www.xiladaili.com/https/'#{page}/'.format(page=random.randint(1,2))
    ipAgent = {
        'http':'http://125.108.123.95:9000'
    }
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
    }
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        # ip_list.append(tds[0].text + ':' + tds[1].text)
        ip_list.append(tds[0].text)
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('https://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'https': proxy_ip}
    return proxies


ipList = get_ip_list()

# 获取网页源代码
def get_page(url):
    data={}
    querystring = {"status":"P"}
    headers = {
        'user-agent': ua.random,
    }
    print(ua.random)
    proxies = get_random_ip(ipList)
    # 加代理版本
    print(proxies)
    try:
        response = s.get(url, headers=headers, params=querystring, proxies = proxies, timeout=8)
        data = response.text
        print(data)
        return data
    except: 
        print("got excepiton")
        data = get_page(url)
        return data
    #response = requests.request("GET", url, headers=headers, params=querystring, proxies = {"http": "http://{}".format(proxy)})

# 解析网页源代码
def parse_page(html):
    html_elem = etree.HTML(html)
    print(html_elem)
    # links = html_elem.xpath('//div[@class="hd"]/a/@href')
    # titles = html_elem.xpath('//div[@class="hd"]/a/span[1]/text()')
    # infos = html_elem.xpath('//div[@class="bd"]/p[1]//text()')
    # roles = [j.strip() for i,j in enumerate(infos) if i % 2 == 0]
    # descritions = [j.strip() for i,j in enumerate(infos) if i % 2 != 0]
    # stars = html_elem.xpath('//div[@class="bd"]/div/span[2]/text()')
    # comments = html_elem.xpath('//div[@class="bd"]/div/span[4]/text()')
    # data = zip(links,titles,roles,descritions,stars,comments)
    #return data


# 保存数据到csv
def save2file(data):
    print("数据写入中", len(data))
    file_exists = os.path.isfile('./data/movie_detail.csv')
    with open('./data/movie_detail.csv', mode='a+') as movie_detail_file:
        fieldnames = ['id', 'title', '导演', '编剧', '主演']
        movie_url_writer = csv.DictWriter(movie_detail_file, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # 如果文件存在 就不写头
        if not file_exists:
            movie_url_writer.writeheader()
        
        movie_url_writer.writerow(data)

#读取csvURL
def getMovieUrl(start) :
    with open('./data/movie_url_file.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
        
        interestingrows=[row[0].split(',')[2] for idx, row in enumerate(spamreader) if idx in range(start, start+STEP) and int(row[0].split(',')[3])==0]
       
        print(interestingrows)
        return interestingrows

#标记为]
def markCrawed(start) :
    with open('./data/movie_url_file.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
        
        interestingrows=[row[0].split(',')[2] for idx, row in enumerate(spamreader) if idx in range(start, start+STEP) and int(row[0].split(',')[3])==0]
       
        print(interestingrows)
        return interestingrows

# 汇总全部条数后一起写入
def collectAndSave(start):
    print('开始读取url文件')
    setpList = []
    for page in range(start,APIEND, STEP): 
        print('正在爬取第 ' + str(page) + ' 部至第 ' + str(page+STEP) + ' 部......')
        urls = getMovieUrl(start)
        for url in urls :
            setpList.append(crawlDetail(url))
            
        # save2file(setpList)
        # markCrawed(setpList)
    print('结束爬取....')   
# 爬取页面
def crawlDetail(url):
    global ipList
    print('开始爬取...' + url)
    res = get_page(url)

    if res.find("上映日期") >=0 :
        #解析页面数据
        data = parse_page(res)
        time.sleep(5)
        #return data
    else: 
        print(res, '要求登录，2s后重新发送请求。爬取id', id)
        ipList = get_ip_list()
        while len(ipList) == 0:
            ipList = get_ip_list()
        print(ipList)
        time.sleep(10)
        crawlDetail(url)
        
        

# 爬取详情页
if __name__ == '__main__':
    collectAndSave(1)
    #print(list(map(getAPIUrl,[{'a':1, "url":'hello'},{"url":'world'}])))