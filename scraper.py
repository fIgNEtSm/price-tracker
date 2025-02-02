from flask import Flask
from bs4 import BeautifulSoup
import requests
from app import app
from database import get_all, db
from message import send_msg

with app.app_context():
    trackers = get_all()

def get_details(url):
    http_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0"
    }

    response = requests.get(url, headers=http_headers)
    website = response.text
    try:
        soup = BeautifulSoup(website, 'html.parser')
        price = float(soup.find("span", class_="a-price-whole").text.replace(",", ""))
        title = soup.find("span", class_="a-size-large product-title-word-break").text.strip()
    except AttributeError:
        return None
    return {"title": title, "price": price}

for tracker in trackers:
    url = tracker['url']
    email = tracker['email']
    required_price = tracker['price']
    product_details = get_details(url)

    if product_details is None:
        print("Price is none")
        continue

    if product_details['price'] < required_price:
        msg = f"Your tracked product:\n\n{product_details['title']}\n\n{url}\n\nPrice: ₹{product_details['price']}.\n\nGO BUY IT!"
        send_msg(to_email=email, msg=msg)
        print("Message sent!")
