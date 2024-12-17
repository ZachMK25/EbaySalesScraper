from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.get("https://signin.ebay.com")

print("Please log in manually. Press Enter in the terminal after you have logged in successfully.")
input("Press Enter to continue...")  # Wait for manual CAPTCHA and login

driver.get("https://www.ebay.com/mys/sold/rf/sort=MOST_RECENTLY_SOLD&filter=ALL&limit=200&period=LAST_90_DAYS")

driver.implicitly_wait(10) # seconds

sold_items = driver.page_source

soup = BeautifulSoup(sold_items, 'lxml')

# sold-item--content div --> listing

# print(sold_items)

# "item-title" --> descriptions
# "item__sold-date" --> date sold
# "item__shipping-price" --> shipping price [+ Shipping (buyer paid $X)] or [+ Shipping]
# "item__price" --> sale price

listings = [soup.find_all("div", class_="sold-item--content")]

f = open("listings.txt", "w")

print(listings)

f.close()

# cleaned_listings = []

f = open("output.txt", "w")

for listing in listings:
    listing_soup = BeautifulSoup(listing, 'lxml')
    
    listing_dict = {
        "title":listing_soup.find("div", class_="item-title").text,
        "date":listing_soup.find("div", class_="item__shipping-price").text,
        "price":listing_soup.find("div", class_="item__price").text
    }
    # cleaned_listings.append(listing_dict)
    
    f.write(listing_dict)
    # f.write(listing)

f.close()

driver.quit()
