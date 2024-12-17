from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

from bs4 import BeautifulSoup

import re

import openpyxl

login = False

if login:

    driver = webdriver.Chrome()

    driver.get("https://signin.ebay.com")

    print("Please log in manually. Press Enter in the terminal after you have logged in successfully.")
    input("Press Enter to continue...")  # Wait for manual CAPTCHA and login

    driver.get("https://www.ebay.com/mys/sold/rf/sort=MOST_RECENTLY_SOLD&filter=ALL&limit=200&period=LAST_90_DAYS")

    driver.implicitly_wait(10) # seconds

    sold_items = driver.page_source

else:
    input_file = open("example.html", "r")

    html = input_file.read()

    input_file.close()

    sold_items = html


soup = BeautifulSoup(sold_items, 'lxml')

# sold-item--content div --> listing

# print(sold_items)

# "item-title" --> descriptions
# "item__sold-date" --> date sold
# "item__shipping-price" --> shipping price [+ Shipping (buyer paid $X)] or [+ Shipping]
# "item__price" --> sale price
# "item__buyer-name" --> buyer name

listings = soup.find_all("div", class_="sold-item--content")

f = open("listings.txt", "w")

# print(listings)

f.close()

# cleaned_listings = []

# f = open("output.txt", "w")

wb = openpyxl.load_workbook()

shipping_regex = r"buyer paid \$([0-9]+\.[0-9]{2})"

for listing in listings:
    print (listing)
    try:
        title = listing.find("h3", class_= "item-title")
        date = listing.find("div", class_="item__sold-date")
        price = listing.find("span", class_="item__price")
        shipping = listing.find("span", class_="item__shipping-price")
        buyer_name = listing.find("div", class_="item__buyer-name")
        
        if shipping:
            match = re.search(shipping_regex, shipping.text.strip())
            
            if match:
                shipping = match.group()
            else:
                shipping = "Free"
            
        listing_dict = {
            "title": title.text.strip() if title else "NO TITLE",
            "date": date.text.strip() if date else "NO DATE",
            "price": price.text.strip() if price else "NO PRICE",
            
            "shipping": shipping.strip() if shipping else "SHIPPING NOT FOUND",
            
            "buyer_name": buyer_name.text.strip() if buyer_name else "NO BUYER"
        }
        
        # f.write(str(listing_dict) + "\n\n\n\n")
        
    except Exception as e:
        print(f"Error parsing listing: {e}")

# f.close()

if login:
    driver.quit()
