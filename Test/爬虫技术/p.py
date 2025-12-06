import requests
from bs4 import BeautifulSoup

# 1. 发送请求（模拟浏览器）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
url = "https://movie.douban.com/top250"

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

# 2. 解析 HTML
soup = BeautifulSoup(response.text, 'lxml')

# 3. 提取电影标题（通过 CSS 选择器或标签）
titles = soup.select('div.hd a span:nth-child(1)')  # 选第一个 span（中文名）

# 4. 打印结果
for i, title in enumerate(titles, 1):
    print(f"{i}. {title.text}")