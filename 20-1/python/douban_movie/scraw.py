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
print(ua.random)
APIEND = 20000

def get_ip_list():
    #国内高匿代理ip网站
    url = 'https://www.kuaidaili.com/free/intr/5/'
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

ipList = get_ip_list()

# 获取网页源代码
def get_page(url):
    querystring = {"status":"P"}
    headers = {
        'user-agent': ua.random,
        'Cookie': 'll="108296"; bid=yCQKy1Zfre0; __utmz=30149280.1590235049.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _vwo_uuid_v2=DB73CB88E1A6E82140889364A5414874F|9b7e19408b6120c2eeb607301bf50be5; __utmc=30149280; __utmc=223695111; push_noty_num=0; push_doumail_num=0; __utmv=30149280.8848; ap_v=0,6.0; __utma=30149280.607930696.1590235049.1597073781.1597160293.7; __utmt=1; __utma=223695111.1743980471.1590235050.1597073781.1597160295.6; __utmz=223695111.1597160295.6.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1597160295%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=9d6e287a985fe453.1590235050.6.1597160317.1597073780.; __utmb=223695111.4.10.1597160295; dbcl2="88489827:i32rzHzDTUI"; ck=db7p; __utmb=30149280.8.10.1597160293'
    }
    proxies = get_random_ip(ipList)
    # 加代理版本
    print(proxies)
    response = requests.request("GET", url, headers=headers, params=querystring, proxies = proxies)
    #response = requests.get(url=url,headers=headers)
    data = response.text
    print(data);
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
                print(data, '遇到数据中断，10s后重新发送请求。开始页码', pageStart)
                time.sleep(10)
                crawlAPI(pageStart)
       
        time.sleep(5)
    print('结束爬取')

# 爬取详情页
if __name__ == '__main__':
    crawlAPI(2480)
    #print(list(map(getAPIUrl,[{'a':1, "url":'hello'},{"url":'world'}])))