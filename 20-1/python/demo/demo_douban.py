import requests
import os
from bs4 import BeautifulSoup
import bs4
from cons import headerChange
import random

def get_ip_list():
    #国内高匿代理ip网站
    url = 'https://www.kuaidaili.com/free/'
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
print(ipList)

def getHTMLTxt(url, flag):
    querystring = {"status":"P"}
    headers = {
        'user-agent': headerChange(),
    }
    proxies = get_random_ip(ipList)
    r = requests.request("GET", url, headers=headers, params=querystring, proxies = proxies)
    #r.encoding = 'utf-8' 
    r = requests.get(url, headers=headers, params=querystring, proxies = proxies)

    try:
        if flag == 1:    #如果传入的是获取评论信息的url
            r.encoding = 'utf-8'      #尝试改变编码
        elif flag == 2:
            r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getComments(url, cmt):          #获取一整页的评论
    count = 0
    html = getHTMLTxt(url, 1)
    soup = BeautifulSoup(html, "html.parser")
    for tagDiv in soup.find_all('div', attrs={'class':'comment'}):
        if isinstance(tagDiv, bs4.element.Tag):
            infoComt = tagDiv.find('p')
            cmt.append(infoComt.text)
            count = count + 1
    return count

def nextPageURL(urlPre):  #根据前一页的url返回的html中找到后一页的url
    html = getHTMLTxt(urlPre, 2)
    try:
        soup = BeautifulSoup(html, "html.parser")
        divTag = soup.find('div', attrs={'id':'paginator', 'class':'center'})   #找到存有下一页url的div标签
        aTag = divTag('a')                                                      #找到存有信息的a标签
        index = len(aTag)                                                       #下一页的url信息在最后一个<a>标签内
        return aTag[index - 1].get('href')
    except:
        return -1


def countOfComments(urlStart):  #根据首页返回的html拿到评论的总条数
    try:
        html = getHTMLTxt(urlStart, 1)
        soup = BeautifulSoup(html, "html.parser")
        #下面代码在各标签中查找到评论的总条数
        liTag = soup.find('li', attrs={'class':'is-active'})
        spanTag = liTag('span')
        strPage = spanTag[0].string
        return eval(strPage[-5:-1])  #这里的切片根据评论总条数的位数来定
    except:
        return 0

def main():
    urlStart = "https://movie.douban.com/subject/10477598/comments?"    #此处comments后的都不要有，包括'?'
    #depth = countOfComments(urlStart)
    depth = 100   #手动设置评论条数，控制时间
    fpath = "../comments.txt"
    cmt = []
    count = 0
    if os.path.exists('../comments.txt'):
        os.remove('../comments.txt')      #因为需要测试，懒得手动删除，所以程序开始时对文件进行删除操作
    urlNext = ""
    print("爬取评论")
    while(count < depth and len(cmt) < depth):
        url = urlStart + urlNext
        count = count + getComments(url, cmt)
        urlNext = nextPageURL(url)
        if urlNext == -1:
            print("意外终止！")
            break
        else:
            print('\r正在爬取评论，进度：{:.2f}%'.format((count * 100) / depth), end = "")
    print("\n爬取成功，进行储存。。。")
    for i in range(len(cmt)):
        try:
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(cmt[i] + '\n')
                print('\r正在储存评论，进度：第{}条，共{}条'.format(i + 1, len(cmt)), end = "")
        except:
            continue

    print("\n评论储存完毕！")

main()
