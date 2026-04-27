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

r = requests.get(URL, headers=HEADERS)
html = r.text

soup = BeautifulSoup(html, "html.parser")

tickets = []

for item in soup.find_all(["article", "li", "div"]):

    text = item.get_text(strip=True)

    keywords = [
        "SixTONES",
        "販売",
        "枚",
        "円"
    ]

    if all(word in text for word in keywords):

        cleaned = text[:300]

        tickets.append(cleaned)

try:
    with open(SAVE_FILE, "r") as f:
        old_data = json.load(f)
except:
    old_data = []

new_tickets = []

for ticket in tickets:
    if ticket not in old_data:
        new_tickets.append(ticket)

if new_tickets:

    for ticket in new_tickets[:3]:

        message = {
            "content": f"""🎫 SixTONESリセール出現！

{ticket}

購入はこちら
{URL}"""
        }

        requests.post(WEBHOOK, json=message)

with open(SAVE_FILE, "w") as f:
    json.dump(tickets, f)
