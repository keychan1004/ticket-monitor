import requests
import os
import json
from bs4 import BeautifulSoup

URL = "https://relief-ticket.jp/events/artist/40/127"

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

SAVE_FILE = "last_seen.json"

# ページ取得
r = requests.get(URL, headers=HEADERS)
html = r.text

soup = BeautifulSoup(html, "html.parser")

tickets = []

# ページ全体テキスト取得
page_text = soup.get_text(" ", strip=True)

# SixTONESページにチケットがある可能性のあるキーワード
keywords = [
    "円",
    "枚",
    "販売",
    "取引"
]

# 条件一致なら保存
if all(word in page_text for word in keywords):

    tickets.append(page_text[:1000])

# 前回データ
try:
    with open(SAVE_FILE, "r") as f:
        old_data = json.load(f)
except:
    old_data = []

# 新規のみ通知
new_tickets = []

for ticket in tickets:
    if ticket not in old_data:
        new_tickets.append(ticket)

# Discord通知
if new_tickets:

    message = {
        "content": f"""🎫 SixTONESリセール検知！

購入はこちら
{URL}"""
    }

    requests.post(WEBHOOK, json=message)

# 保存
with open(SAVE_FILE, "w") as f:
    json.dump(tickets, f)
