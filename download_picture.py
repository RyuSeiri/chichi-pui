import requests
from bs4 import BeautifulSoup
import urllib

# 输入要爬取的网页url
url = "https://chichi-pui.com/"

# 发送请求并获取响应
response = requests.get(url)

# 使用BeautifulSoup库解析html
soup = BeautifulSoup(response.content, "html.parser")

# 查找所有的img标签
img_tags = soup.find_all("img")

# 遍历所有的img标签，获取图片url并下载
for img in img_tags:
    img_url = img.get("src")
    if img_url is not None and img_url.startswith("http"):
        # 将图片url转换为文件名
        img_name = img_url.split("/")[-1]
        # 使用urllib库将图片下载到本地
        urllib.request.urlretrieve(img_url, img_name)
