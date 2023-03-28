# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("https://chichi-pui.com/")

# user_ids = []

# while True:
#     try:
#         # 等待"Load More"按钮出现，并点击该按钮
#         load_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
#             (By.XPATH, "//button[contains(text(), 'Load More')]")))
#         load_more_button.click()

#         # 等待新页面加载完毕
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#             (By.XPATH, "//a[@class='post-card']")))

#         # 解析当前页面，获取所有用户ID
#         user_links = driver.find_elements_by_xpath("//a[@class='post-card']")
#         for link in user_links:
#             href = link.get_attribute("href")
#             user_id = href.split("/")[-1]
#             user_ids.append(user_id)

#     except:
#         # 如果没有"Load More"按钮或者按钮无法点击，退出循环
#         break

# driver.quit()

# print(user_ids)
import requests
from bs4 import BeautifulSoup

url = "https://www.chichi-pui.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

image_urls = []
for img in soup.find_all("img"):
    src = img.get("src")
    if src and "storage/" in src:
        image_urls.append(src)

# 现在您有了所有用户上传的图像的URL列表。您可以使用requests库下载它们。
for i, image_url in enumerate(image_urls):
    response = requests.get(image_url)
    with open(f"image_{i}.jpg", "wb") as f:
        f.write(response.content)
