# this is utils

import traceback
import telegram
import datetime
import time
import requests
import json
from Bot.models import UserInfo

global bot
global TOKEN
TOKEN = '5761837078:AAE8swqpRKGalpjwOaM4RKZXtDHIWn3-654'
bot = telegram.Bot(token= TOKEN)




def data_retriver(tracking_id):
    url = "https://ekartlogistics.com/ws/getTrackingDetails"
    payload = json.dumps({
      "trackingId": tracking_id 
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    print(type(data))
    print(data)
    return data

# len_data = 0
# count = 0
# while True:
#     try:
#         data = process_data()
#         if len_data != len(data):
#             len_data = len(data)
#             last_data = data[-1]
#             last_data_time = last_data['date']/1000
#             date = str(datetime.datetime.fromtimestamp(last_data_time))
#             reply_text = f"You package's last update is:-\n\nLocation:- {last_data['city']}\nTime:- {date}\nUpdate:- {last_data['statusDetails']}"
#             print(bot.sendMessage(chat_id='5651819129',text=reply_text))
#         elif not count%12:
#             reply_text = "No new update in last 1 hour!"
#             print(bot.sendMessage(chat_id='5651819129',text=reply_text))
#     except:
#         import traceback
#         print(bot.sendMessage(chat_id='5651819129',text=str(traceback.format_exc())))
#     count += 1
#     print(count)
#     time.sleep(300)
    # FMPP1404885384

'''{'shipmentType': 'Forward', 'expectedDeliveryDate': 1682087890000, 'receiverName': 'ShaanRawat', 'receiverRelationShip': None, 
'merchantName': 'flipkart.com', 'sourceCity': 'JAIPUR', 'destinationCity': 'Gurgaon', 'reachedNearestHub': True, 'faShipment': False, 
'shipmentTrackingDetails': [{'date': 1681868973000, 'city': 'JAIPUR', 'statusDetails': 'Shipment Created'}, 
{'date': 1681905458000, 'city': 'JAIPUR', 'statusDetails': 'Pickup From Seller'}, {'date': 1681936437000, 'city': 'JAIPUR', 'statusDetails': 'Received at FKL_Jaipur_BTS'}, 
{'date': 1681868976000, 'city': 'Jaipur', 'statusDetails': 'Dispatched to JAI/BTS'}, {'date': 1681936441000, 'city': 'Jaipur', 'statusDetails': 'Received at JAI/BTS'}, 
{'date': 1681937136000, 'city': 'Jaipur', 'statusDetails': 'Received at JAI/BTS'}, {'date': 1681975155000, 'city': 'New Delhi', 'statusDetails': 'Dispatched to Bamnoli Sort Centre'}, 
{'date': 1682011250000, 'city': 'New Delhi', 'statusDetails': 'Received at Bamnoli Sort Centre'}, {'date': 1682025970000, 'city': 'Gurgaon', 'statusDetails': 'Dispatched to Badshahpur Hub'}, 
{'date': 1682037452000, 'city': 'Gurgaon', 'statusDetails': 'Received at Badshahpur Hub'}, {'date': 1682043362000, 'city': 'Gurgaon', 'statusDetails': 'Out For Delivery'},
{'date': 1682087890000, 'city': 'Gurgaon', 'statusDetails': 'Delivered'}]}'''

def processed_data(tracking_id):
  try:
    data = data_retriver(tracking_id)
    print(type(data),data)
    exp_date = data.get('expectedDeliveryDate')
    exp_date = exp_date/1000
    expected_date = str(datetime.date.fromtimestamp(exp_date))
    print('\n\\\\',exp_date,expected_date)
    data_shipment = data['shipmentTrackingDetails']
    #print('$$$$$', data_shipment, '$$$$$')
    data_list = list(data_shipment)
    print('@@@',type(data_list),data_list,'@@@')
    last_data = data_list[-1]
    #print('***',last_data,'***')
    latest_date = last_data['date']/1000
    date = str(datetime.datetime.fromtimestamp(latest_date))
    #print("&&", date ,'&&')
    merchant = data['merchantName']
    reply_text = f"Latest update for your package from {merchant} is:-\n\nLocation:- {last_data['city']}\nLast updated on:- {date}\nExpected date:- {expected_date}\nStatus Update:- {last_data['statusDetails']}"
    print('pass')
  except:
     reply_text = 'Error! Could not fetch data!'
     print(traceback.format_exc())
  
  return reply_text

def get_history(chat_id):
  print('history----->')
  try:
    history = UserInfo.objects.filter(chat_id=chat_id)
    count = 1
    reply_text = "Hi! Your history is:"
    for i in history:
      print(i.__dict__)
      reply_text +=  f"\n{count}. {i.tracking_id}"
      count += 1
  except UserInfo.DoesNotExist:
    reply_text = 'Entry does not exist.'
  return reply_text

def del_history(chat_id, entry_to_be_del):
  print('history to be deleted>>>>>>>>>')
  try:
    del_entry = UserInfo.objects.filter(chat_id=chat_id)[entry_to_be_del]
    print(del_entry)
    del_entry.delete()
    reply_text = 'Entry deleted!'

  except UserInfo.DoesNotExist:
    reply_text = 'Entry does not exist.'
  except IndexError:
    reply_text = 'Entry does not exist.'
  
  return reply_text

def del_all(chat_id):
  try:
    UserInfo.objects.filter(chat_id=chat_id).delete()
    reply_text = 'All entries deleted!'
  except UserInfo.DoesNotExist:
    reply_text = 'User history does not exist.'
  except IndexError:
    reply_text = 'Entry does not exist.'
  return reply_text
