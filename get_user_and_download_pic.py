import os
import requests
from bs4 import BeautifulSoup

# 用户主页的url格式
user_url_format = "https://chichi-pui.com/user/{}"

# 获取所有用户的id
response = requests.get("https://chichi-pui.com")
html = response.text
soup = BeautifulSoup(html, "html.parser")
user_ids = [a.get("href").split("/")[-1] for a in soup.find_all("a", href=True) if a.get("href").startswith("/user/")]

# 循环获取每个用户的图片
for user_id in user_ids:
    # 构造用户主页的url
    user_url = user_url_format.format(user_id)
    
    # 发送请求并获取html代码
    response = requests.get(user_url)
    html = response.text
    
    # 解析html代码，获取所有图片的url
    soup = BeautifulSoup(html, "html.parser")
    image_urls = []
    for img in soup.find_all("img"):
        image_url = img.get("src")
        if image_url and image_url.startswith("https://"):
            image_urls.append(image_url)
    
    # 下载所有图片，并保存到以用户id命名的文件夹中
    if image_urls:
        user_folder = user_id
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)
        for i, image_url in enumerate(image_urls):
            image_name = f"{i+1}.jpg"
            image_path = os.path.join(user_folder, image_name)
            response = requests.get(image_url)
            with open(image_path, "wb") as f:
                f.write(response.content)
