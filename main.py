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

# Relief Ticket用に広めに拾う
for item in soup.find_all(["article", "li", "div", "section"]):

    text = item.get_text(" ", strip=True)

    #
