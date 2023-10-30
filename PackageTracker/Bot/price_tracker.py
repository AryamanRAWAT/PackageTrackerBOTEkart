from os import path
import requests
from bs4 import BeautifulSoup
import time
from helium import *
def tracker(url):
    browser = start_chrome(url, headless=True)
    html = browser.page_source
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    if 'www.amazon.in' in url:
        price = soup.find(class_='a-price-whole')
        currency = soup.find(class_='a-price-symbol')
        print(currency.text+price.text)
        return 'Current price -> ' + currency.text+price.text
    elif 'www.flipkart.com' in url:
        price = soup.find(class_='_30jeq3 _16Jk6d')
        print(price.text)
        return 'Current price -> ' + price.text
    browser.quit()
        