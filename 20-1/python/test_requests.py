import requests

url = 'https://movie.douban.com/subject/26871906/?tag=%E7%83%AD%E9%97%A8&from=gaia'
#url = 'https://cloud.tencent.com/developer/article/1562566'
# 获取网页内容
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "bid=Zit3B7UG0aQ; ll='108296'; _vwo_uuid_v2=D51BD83219CEF9F6A83F6A48D3D065F79|8b3daab3cb38226c2c9054c86639c87f; _ga=GA1.2.77902144.1587720491; gr_user_id=2c0d18cd-4640-41cb-b4ab-c775ecc6baef; douban-fav-remind=1; __utmc=30149280; __utmc=223695111; viewed=\'3264665_27185420_30135873\'; ct=y; dbcl2='88489827:UBdXA/efPRo'; ck=ujBq; push_noty_num=0; push_doumail_num=0; __utmv=30149280.8848; ap_v=0,6.0; __utma=30149280.77902144.1587720491.1596694474.1596697404.17; __utmz=30149280.1596697404.17.7.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=30149280.6.10.1596697404; __utma=223695111.1632482409.1590565138.1596697404.1596701003.9; __utmb=223695111.0.10.1596701003; __utmz=223695111.1596701003.9.9.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1596701003%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=1ea1a78bb5a2a9a4.1590565138.9.1596701049.1596698020.",
    "Host": "movie.douban.com",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
               }
# 设置headers
response = requests.get(url = url, headers = headers)
#response = requests.get(url)
# 获取网页相关信息
#response.encoding = 'ISO-8859-1'
#print(response.headers)
#print(response.cookies)
#print(response.status_code)
print(response.encoding)
print(response.text)
