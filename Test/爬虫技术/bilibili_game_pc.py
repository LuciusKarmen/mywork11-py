import requests

# ✅ 正确的 API 地址（你抓到的）
url = "https://le3-api.game.bilibili.com/pc/game/ranking/page_ranking_list"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Referer": "https://game.bilibili.com/platform/ranks",
    "Origin": "https://game.bilibili.com"
}

params = {
    "ranking_type": 11,   # 11 = 热门游戏榜
    "page_num": 1,
    "page_size": 50       # 最多一次50条
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    if data.get("code") == 0:  # B站用 code=0 表示成功
        games = data["data"]["client_game_list"]
        print(f"✅ 共找到 {len(games)} 款游戏：\n")
        for i, game in enumerate(games, 1):
            # 提取游戏名称（注意字段名！）
            name = game["title"]
            grade = game.get("grade", "N/A")  # 评分
            comments = game.get("valid_comment_number", 0)  # 评论数
            print(f"{i:2d}. {name:<25} | 评分: {grade} | 评论数: {comments}")
    else:
        print("❌ API 返回业务错误:", data.get("message"))
else:
    print("❌ HTTP 请求失败，状态码:", response.status_code)