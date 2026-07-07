import json
import os

FILE = "products.json"


def init_db():
    if not os.path.exists(FILE):
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump([], f)


def add_product(url, name, price):
    products = get_products()

    products.append({
        "url": url,
        "name": name,
        "price": price
    })

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)


def get_products():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def update_price(url, price):
    products = get_products()

    for p in products:
        if p["url"] == url:
            p["price"] = price

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)