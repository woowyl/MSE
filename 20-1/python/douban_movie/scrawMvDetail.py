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

ua = UserAgent(verify_ssl=False)
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))

APIEND = 30000
#每次读取的长度
STEP = 20
ipList = []
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

def get_ip_list2():
    #国内高匿代理ip网站
    url = 'http://dev.qydailiip.com/api/?apikey=2dfe40deb680d0f6167b0a9abe6525a2557a8944&num=30&type=json&line=mac&proxy_type=putong&sort=1&model=all&protocol=https&address=&kill_address=&port=&kill_port=&today=true&abroad=1&isp=1&anonymity='#{page}/'.format(page=random.randint(1,2))
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
    }
    #web_data = requests.get(url, headers=headers, proxies = ipAgent)
    web_data = requests.get(url, headers=headers)
    print(json.loads(web_data.text))
    return json.loads(web_data.text)

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('https://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'https': proxy_ip}
    return proxies


ipList = get_ip_list()
proxies = get_random_ip(ipList)
# 获取网页源代码
def get_page(url, changeProxy):
    global proxies
    data={}
    querystring = {"status":"P"}
    headers = {
        'user-agent': ua.random,
    }
    print(ua.random)
    if changeProxy:
        proxies = get_random_ip(ipList)
    # 加代理版本
    print(proxies)
    loop = 1
    while loop > 0:
        try:
            print("try", url)
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
    #response = requests.request("GET", url, headers=headers, params=querystring, proxies = {"http": "http://{}".format(proxy)})

# 解析网页源代码
def parse_page(html):
    with open('./data/log.csv', mode='a+') as movie_detail_file:
        movie_url_writer = csv.writer(movie_detail_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # 如果文件存在 就不写头
        movie_url_writer.writerow([html])

    film = {}
    html_elem = etree.HTML(html)
    film['title'] = '/'.join(html_elem.xpath('//span[@property="v:itemreviewed"]/text()'))
    film['year'] = '/'.join(html_elem.xpath('//span[@class="year"]/text()')).replace('(','').replace(')', '')
    film['director'] = '/'.join(html_elem.xpath('//a[@rel="v:directedBy"]/text()'))
    film['screenwriter'] = '/'.join(html_elem.xpath('//div[@id="info"]/span[2]/span[@class="attrs"]/a/text()'))
    film['actors'] = '/'.join(html_elem.xpath('//div[@id="info"]/span[@class="actor"]/span[@class="attrs"]/a[@rel="v:starring"]/text()'))
    film['type'] = '/'.join(html_elem.xpath('//div[@id="info"]/span[@property="v:genre"]/text()'))
    film['runtime'] = '/'.join(html_elem.xpath('//div[@id="info"]/span[@property="v:runtime"]/text()'))
    film['pubtime'] = '/'.join(html_elem.xpath('//div[@id="info"]/span[@property="v:initialReleaseDate"]/text()'))
    film['country'] = getFistEleFromList(html_elem.xpath('//*[@id="info"]/text()[preceding-sibling::span[contains(text(), "制片国家/地区:")] and following-sibling::br]'))
    # film['alias'] = getFistEleFromList(html_elem.xpath('//*[@id="info"]/text()[preceding-sibling::span[contains(text(), "制片国家/地区:")] and following-sibling::br]'))
    film['language'] = getFistEleFromList(html_elem.xpath('//*[@id="info"]/text()[preceding-sibling::span[contains(text(), "语言:")] and following-sibling::br]'))
    film['scoreNum'] = getFistEleFromList(html_elem.xpath('//span[@property="v:votes"]/text()'))
    film['score'] = getFistEleFromList(html_elem.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()'))
    film['star5'] =getFistEleFromList(html_elem.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[1]/span[2]/text()'))
    film['star4'] =getFistEleFromList(html_elem.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[2]/span[2]/text()'))
    film['star3'] =getFistEleFromList(html_elem.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[3]/span[2]/text()'))
    film['star2'] =getFistEleFromList(html_elem.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[4]/span[2]/text()'))
    film['star1'] =getFistEleFromList(html_elem.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[5]/span[2]/text()'))
    film['smallCommentNum'] = getDigit('/'.join(html_elem.xpath('//*[@id="comments-section"]/div[1]/h2/span/a/text()')))
    film['longCommentNum'] = getDigit('/'.join(html_elem.xpath('//*[@id="reviews-wrapper"]/header/h2/span/a/text()')))
    film['posterurl'] = getFistEleFromList(html_elem.xpath('//img[@rel="v:image"]/@src'))
    film['summary'] = '/'.join(getFistEleFromList(html_elem.xpath('//*[@id="link-report"]/span/text()'))).strip().replace('\n', '').replace('\r', '')
    #return data
    print("film data ==",film)
    return film

def getDigit(str):
    return ''.join([x for x in str if x.isdigit()])

def getFistEleFromList(list): 
    if len(list) > 0 : 
        return list[0]
    else :
        return ''

# 保存数据到csv
def save2file(data):
    print("数据写入中,写入长度:", len(data))
    file_exists = os.path.isfile('./data/movie_detail_2018.csv')
    with open('./data/movie_detail_2018.csv', mode='a+') as movie_detail_file:
        fieldnames = ['title', 'year', 'director', 'screenwriter', 'actors','type','summary', 'runtime', 'pubtime', 'country', 'language', 'scoreNum', 'score', 'star5', 'star4', 'star3', 'star2', 'star1', 'smallCommentNum', 'longCommentNum', 'posterurl']
        movie_url_writer = csv.DictWriter(movie_detail_file, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # 如果文件存在 就不写头
        if not file_exists:
            movie_url_writer.writeheader()
        for item in data:
            if isinstance(item, dict):
                movie_url_writer.writerow(item)

#读取csvURL
def getMovieUrl(start) :
    with open('./data/movie_url_file_2018.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\n', quotechar=',')
        
        #interestingrows=[row for idx, row in enumerate(spamreader) if idx in range(start, start+STEP)]
        interestingrows=[row[0].split(',')[3] for idx, row in enumerate(spamreader) if idx in range(start, start+STEP)]
       
        print(interestingrows)
        return interestingrows

# 汇总全部条数后一起写入
def collectAndSave(start):
    print('开始读取url文件')
    setpList = []
    for page in range(start,APIEND, STEP): 
        print('正在爬取2018年第' + str(page) + '部至第' + str(page+STEP-1) + ' 部......')
        urls = getMovieUrl(page)
        for url in urls :
            movie = crawlDetail(url, False)
            setpList.append(movie)
        save2file(setpList)
        setpList = []
        # markCrawed(setpList)
    print('结束爬取....')   
# 爬取页面
def crawlDetail(url, keepalive):
    global ipList
    print('\n开始爬取......' + url)
    loop = 1
    changeProxy = False
    failNum = 0
    while loop > 0:
        if failNum > 10:
            ipList = get_ip_list()
            while len(ipList) == 0:
                ipList = get_ip_list()
            print("失败次数超过10次，重新爬取代理",ipList)
        res = get_page(url, changeProxy)

        if res.find("我要写短评") >=0 :
            #解析页面数据
            data = parse_page(res)
            time.sleep(5)
            loop = 0
            return data
        else: 
            print(res, '要求登录，2s后重新发送请求。爬取url', url)
            changeProxy = True
            failNum = failNum +1
            time.sleep(2)
            

# 爬取详情页
if __name__ == '__main__':
    collectAndSave(1)
    