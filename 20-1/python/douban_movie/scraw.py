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

#ua = UserAgent(use_cache_server=False) 
ua = UserAgent(verify_ssl=False) 
#print(ua.random)
APIEND = 20000
ipList = []
def get_ip_list():
    #国内高匿代理ip网站
    url = 'https://www.kuaidaili.com/free/intr/{page}/'.format(page=random.randint(1,3000))
    print(url)
    ipAgent = {
        'http':'https://60.216.20.211:8001'
    }
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
    }
    web_data = requests.get(url, headers=headers, proxies = ipAgent)
    soup = BeautifulSoup(web_data.text, 'lxml')
    #print(soup)
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[0].text + ':' + tds[1].text)
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

#ipList = get_ip_list()
print(ipList)

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


# 获取网页源代码
def get_page(url):
    querystring = {"status":"P"}
    headers = {
        'user-agent': ua.random,
    }
    #proxies = get_random_ip(ipList)
    proxy = get_proxy().get("proxy")
    # 加代理版本
    print("http://{}".format(proxy))
    # response = requests.request("GET", url, headers=headers, params=querystring, proxies = proxies)
    response = requests.request("GET", url, headers=headers, params=querystring, proxies = {"http": "http://{}".format(proxy)})
    #response = requests.get(url=url,headers=headers)
    data = response.text
    return data

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


# 保存数据到csv
def save2file(data):
    print("本次写入数据长度：", len(data))
    file_exists = os.path.isfile('./data/movie_url_file.csv')
    with open('./data/movie_url_file.csv', mode='a+') as movie_url_file:
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
    url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={page}&year_range=2020,2020'
    print('开始爬取')
    for page in range(pageStart,APIEND,20):
        print('正在爬取第 ' + str(page) + ' 部至第 ' + str(page+20) + ' 部......')
        res = get_page(url.format(page=str(page)))
        data = json.loads(res).get("data")
        if data:
            movieUrls = list(map(getAPIUrl,data))
            save2file(movieUrls)
            pageStart = page+20
        else:
            if isinstance(data, list) and len(data) == 0:
                break
            else:
                print(data, '遇到数据中断，8s后重新发送请求。开始页码', pageStart)
                ipList = get_ip_list()
                while len(ipList) == 0:
                    ipList = get_ip_list()
                
                print(ipList)
                time.sleep(8)
                crawlAPI(pageStart)
       
        time.sleep(5)
    print('结束爬取')

# 爬取详情页
if __name__ == '__main__':
    crawlAPI(2800)
    #print(list(map(getAPIUrl,[{'a':1, "url":'hello'},{"url":'world'}])))