# coding: utf-8
import requests 
import json
from lxml import etree
import csv
import time 
import random
from bs4 import BeautifulSoup
import bs4
import os.path
from fake_useragent import UserAgent  
from requests.adapters import HTTPAdapter

scrawUrlStartYear = 2010
scrawUrlEndYear = 2016
scrawStartPage = 6649

ua = UserAgent(use_cache_server=False) 
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))

APIEND = 20000
ipList = []
proxies = {}
def get_ip_list():
     #国内高匿代理ip网站
    # url = 'http://www.xiladaili.com/https/'#{page}/'.format(page=random.randint(1,2))
    url = 'http://www.nimadaili.com/https/'#{page}/'.format(page=random.randint(1,2))
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
        # ip_list.append(tds[0].text.replace("\n",'').replace("\t", "") + ':' + tds[1].text.replace("\n",'').replace("\t", ""))
        ip_list.append(tds[0].text)
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('https://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxiesInner = {'https': proxy_ip}
    return proxiesInner


ipList = get_ip_list()
proxies = get_random_ip(ipList)

# 获取网页源代码
def get_page(url, proxyChange):
    global proxies
    data={}
    querystring = {"status":"P"}
    headers = {
        'user-agent': ua.random,
    }
    print(ua.random)
    if proxyChange:
        proxies = get_random_ip(ipList)
    # 加代理版本
    print(proxies)
    loop = 1
    while loop > 0:
        try:
            response = s.get(url, headers=headers, params=querystring, proxies = proxies, timeout=8)
            data = response.text
            loop = 0
            return data
        except: 
            loop = loop +1
            if loop > 3:
                proxies = get_random_ip(ipList)
            print("got excepiton")
            time.sleep(1)

# 保存数据到csv
def save2file(data):
    print("本次写入数据长度：", len(data))
    file_exists = os.path.isfile('./data/movie_url_file_{start}_{end}.csv'.format(start=str(scrawUrlStartYear), end=str(scrawUrlEndYear)))
    with open('./data/movie_url_file_{start}_{end}.csv'.format(start=str(scrawUrlStartYear), end=str(scrawUrlEndYear)), mode='a+') as movie_url_file:
        fieldnames = ['id', 'title', 'url', 'isCrawed']
        movie_url_writer = csv.DictWriter(movie_url_file, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # 如果文件存在 就不写头
        if not file_exists:
            movie_url_writer.writeheader()

        for item in data:
            movie_url_writer.writerow(item)


# 解析接口的字段
def getAPIUrl(x):
    return {
        'id': x['id'],
        'url': x['url'],
        'title': x['title'],
        'isCrawed': 0
    }

# 爬取接口
def crawlAPI(start):
    global ipList
    pageStart = start
    url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={page}&year_range='+str(scrawUrlStartYear)+','+str(scrawUrlEndYear)
    print('开始爬取')
    running = 1
    needChangeProxy = False
    failNum = 0
    while running == 1 :
        if failNum > 20:
            ipList = get_ip_list()
            while len(ipList) == 0:
                ipList = get_ip_list()
            print("重试次数已达到上限20,重新获取列表：",ipList)

        print('正在爬取第 ' + str(pageStart) + ' 部至第 ' + str(pageStart+20) + ' 部......')
        res = get_page(url.format(page=str(pageStart)), needChangeProxy)
        if res.find("登录") >= 0:
            failNum = failNum +1
            print(res, '要求登录，10s后重新发送请求。开始页码', pageStart)
            needChangeProxy = True
            time.sleep(10)
        else :
            data = json.loads(res).get("data")
            if data:
                needChangeProxy = False
                movieUrls = list(map(getAPIUrl,data))
                save2file(movieUrls)
                pageStart = pageStart+20
                time.sleep(3)
            else:
                if isinstance(data, list) and len(data) == 0:
                    running = 0
                    break
                else:
                    print(data, '遇到数据中断，10s后重新发送请求。开始页码', pageStart)
                    needChangeProxy = True
                    failNum = failNum +1
                    time.sleep(10)
    print('结束爬取')

# 爬取详情页
if __name__ == '__main__':
    crawlAPI(scrawStartPage)
    #print(list(map(getAPIUrl,[{'a':1, "url":'hello'},{"url":'world'}])))