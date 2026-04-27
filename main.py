import requests
import os

URL = "https://relief-ticket.jp/events/artist/40/127"

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(URL, headers=headers)

message = {
    "content": f"""✅ Relief Ticket接続確認

Status Code: {r.status_code}

URL:
{URL}

ページ長さ:
{len(r.text)}
"""
}

requests.post(WEBHOOK, json=message)
