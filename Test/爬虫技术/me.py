from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 设置无头模式（不弹出浏览器窗口）
options = Options()
options.add_argument("--headless")  # 后台运行
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # 打开你的网站
    driver.get("http://xingchengnet.online:8889")

    # 等待 JS 渲染完成（关键！）
    time.sleep(3)  # 或用 WebDriverWait 更精准

    # 获取整个页面的文本内容
    page_text = driver.find_element(By.TAG_NAME, "body").text
    print("爬取到的内容：")
    print(page_text)

finally:
    driver.quit()