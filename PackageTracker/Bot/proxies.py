# q = queue.Queue()
# lst = p.split('\n')
# valid_proxy = []
# for i in p:
#     q.put(i)

# def check_ip():
#     global q
#     while not q.empty():
#         proxy = q.get()
#         try:
#             res = requests.get('http://ipinfo.io/json',
#                                proxies={"http": proxy,
#                                         "https": proxy})
#         except:
#             continue

#         if res.status_code == 200:
#             print(proxy)


# for _ in range(10):
#     threading.Thread(target=check_ip).start()


import requests
import random
import csv
import concurrent.futures



proxylist = []

with open('Bot\proxylist.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])

def extract(proxy):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:
        r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=2)
        print(r.json(), ' | Works')
    except:
        pass
    return proxy

with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract, proxylist)
