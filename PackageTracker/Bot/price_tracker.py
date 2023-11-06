from os import path
import traceback
import requests
from bs4 import BeautifulSoup
import time
from helium import *
import time
import sqlite3
def tracker(url, chat_id, product_url):

    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    is_active = cursor.execute(f"SELECT is_active FROM Bot_userprice WHERE chat_id = '{chat_id}' AND product_url = '{product_url}'")
    count = 0

# Method to compare and update price.  
    def price_comp(currency,price):
        latest_db_price = cursor.execute(f"SELECT latest_price FROM Bot_userprice WHERE chat_id = '{chat_id}' AND product_url = '{product_url}'")
        prev_price = latest_db_price.fetchone()
        prev_price = prev_price[0]
        print(';;;;;;',prev_price, type(prev_price))
        
        if prev_price is not None:
            prev_price = int(prev_price[1:])
            if price > prev_price:
                cursor.execute(f"UPDATE Bot_userprice SET latest_price = '{currency+str(price)}' WHERE chat_id = '{chat_id}' AND product_url = '{product_url}'")
                connection.commit()
                reply_text =  f"<b>PRICE HIKE!!!!\n Previous price = {prev_price}\n Latest price = {price}\n Price hiked by {currency,price-prev_price}</b>"
            
            elif price < prev_price:
                cursor.execute(f"UPDATE Bot_userprice SET latest_price = '{currency+str(price)}' WHERE chat_id = '{chat_id}' AND product_url = '{product_url}'")
                connection.commit()
                reply_text =  f"<b>PRICE DROP!!!!\n Previous price = {prev_price}\n Latest price = {price}\n Price reduced by {currency,prev_price-price}</b>"
            
            else:
                reply_text =  f"No change.\n Latest price is {currency,prev_price}"
        else:
            cursor.execute(f"UPDATE Bot_userprice SET latest_price = '{currency+str(price)}' WHERE chat_id = '{chat_id}' AND product_url = '{product_url}'")
            connection.commit()
            reply_text =  f"Tracking now....\n Latest price is {currency,price}"
        print(reply_text)
        return reply_text
    
# loop code to check price for updates in intervals
    while is_active:
        try:    
            browser = start_chrome(url, headless=True)
            html = browser.page_source
            # print(html)
            soup = BeautifulSoup(html, 'html.parser')
            
            if 'www.amazon.in' in url:
                price_s = soup.find(class_='a-price-whole')
                currency = soup.find(class_='a-price-symbol')
                price = ''
                for i in price_s.text:
                    if i.isdigit():
                        price += ''.join(i)
                reply_text =  price_comp(currency,int(price))
            
            elif 'www.flipkart.com' in url:
                price_s = soup.find(class_='_30jeq3 _16Jk6d')
                currency = price_s.text[0]
                price = ''
                for i in price_s.text:
                    if i.isdigit():
                        price += ''.join(i)
                print('flipkart')
                print(price, type(price))
                reply_text =  price_comp(currency,int(price))
            browser.quit()
            count = 0
            print('sleep')
            print(reply_text)
            time.sleep(30)
            
            return reply_text
        
        except:
            count += 1
            if count <= 5:
                print('Retrying....', count)
                print(traceback.format_exc())
                continue
            else:
                print(traceback.format_exc())
                reply_text =  'Error! Could not fetch data!'
                return reply_text
    
