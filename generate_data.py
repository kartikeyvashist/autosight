import csv
import random
from datetime import datetime, timedelta

products = {
    "Laptop": (50000, 70000),
    "Mouse": (500, 1500),
    "Keyboard": (1500, 4000),
    "Monitor": (10000, 20000),
    "Headphones": (2000, 6000)
}

start_date = datetime(2025, 1, 1)
rows = []

for i in range(30):
    date = start_date + timedelta(days=i)

    for product, price_range in products.items():
        quantity = random.randint(5, 40)
        price = random.randint(*price_range)

        rows.append([
            date.strftime("%Y-%m-%d"),
            product,
            quantity,
            price
        ])

with open("sales_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["sale_date", "product_name", "quantity", "price"])
    writer.writerows(rows)

print("Multi-product realistic 30-day dataset generated.")