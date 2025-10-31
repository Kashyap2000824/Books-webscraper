import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.flipkart.com/search?q=laptop"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

products = []
for item in soup.select("div._1AtVbE"):
    name = item.select_one("div._4rR01T")
    price = item.select_one("div._30jeq3")
    rating = item.select_one("div._3LWZlK")
    link = item.select_one("a._1fQZEK")

    if name and price and link:
        products.append({
            "Product Name": name.text.strip(),
            "Price": price.text.strip(),
            "Rating": rating.text.strip() if rating else "No rating",
            "Link": "https://www.flipkart.com" + link["href"]
        })

df = pd.DataFrame(products)
df.to_csv("flipkart_laptops.csv", index=False)