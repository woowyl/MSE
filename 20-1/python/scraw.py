# 引入库
from urllib import request
import chardet

# 发送请求并接收响应
response = request.urlopen("https://www.fanli.com/")
# # 调用read方法读取并转换为utf8编码
# html = response.read()
# # 获取文本编码s
# html_encoding = chardet.detect(html)
# # 文本转换编码
# content = html.decode(html_encoding['encoding'])
print("content")