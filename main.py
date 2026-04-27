import requests
import os

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

message = {
    "content": "✅ Discord通知テスト成功"
}

requests.post(WEBHOOK, json=message)
