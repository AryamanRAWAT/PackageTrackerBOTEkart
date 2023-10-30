# import threading
# import requests
# import queue

# p = """50.206.25.109:80
# 50.206.25.107:80
# 211.128.96.206:80
# 107.1.93.221:80
# 50.171.32.230:80
# 50.218.57.66:80
# 12.186.205.120:80
# 50.207.199.82:80
# 50.221.230.186:80
# 50.207.199.87:80
# 50.168.49.109:80
# 195.23.57.78:80
# 50.170.90.31:80
# 43.157.8.79:8888
# 85.8.68.2:80
# 191.243.46.162:43241
# 50.174.145.12:80
# 107.1.93.223:80
# 50.207.199.81:80
# 185.160.26.114:80
# 81.23.114.238:8080
# 64.201.163.133:80
# 50.206.111.90:80
# 50.222.245.50:80
# 50.223.38.2:80
# 24.158.29.166:80
# 50.222.245.44:80
# 50.200.12.86:80
# 213.143.113.82:80
# 212.107.31.118:80
# 107.1.93.209:80
# 50.171.32.227:80
# 118.69.111.51:8080
# 50.168.210.236:80
# 113.161.131.43:80
# 50.168.163.182:80
# 107.1.93.220:80
# 50.222.245.45:80
# 50.169.23.170:80
# 50.228.83.226:80
# 50.169.115.53:80
# 50.168.49.104:80
# 50.168.49.107:80
# 50.168.210.238:80
# 50.170.90.34:80
# 51.15.242.202:8888
# 50.169.37.50:80
# 50.168.210.235:80
# 12.186.205.122:80
# 50.207.199.83:80
# 155.0.72.251:3128
# 50.169.62.104:80
# 213.33.2.28:80
# 172.108.208.74:80
# 50.227.121.32:80
# 50.204.219.227:80
# 35.236.207.242:33333
# 50.237.207.186:80
# 50.169.115.49:80
# 50.217.29.198:80
# 107.1.93.212:80
# 50.168.72.122:80
# 50.228.141.98:80
# 41.230.216.70:80
# 50.222.245.46:80
# 50.168.72.112:80
# 50.206.25.104:80
# 50.169.62.111:80
# 50.204.219.230:80
# 82.119.96.254:80
# 50.238.154.98:80
# 50.222.245.47:80
# 8.209.114.72:3129
# 50.174.41.66:80
# 139.59.1.14:8080
# 50.169.62.107:80
# 50.227.121.34:80
# 50.206.25.108:80
# 50.204.190.234:80
# 24.205.201.186:80
# 50.171.32.231:80
# 50.227.121.38:80
# 213.233.177.134:80
# 178.21.163.24:80
# 27.79.56.106:10004
# 50.204.219.226:80
# 50.218.57.71:80
# 50.169.115.51:80
# 50.169.62.106:80
# 15.204.161.192:18080
# 50.222.245.43:80
# 50.168.72.119:80
# 50.206.111.91:80
# 50.169.62.105:80
# 50.207.199.85:80
# 50.168.163.176:80
# 50.222.245.41:80
# 62.99.138.162:80
# 107.1.93.222:80
# 45.39.72.226:3128
# 154.84.142.193:3128
# 156.239.48.24:3128
# 156.239.53.155:3128
# 181.209.110.190:999
# 194.182.169.100:80
# 156.239.52.102:3128
# 139.255.94.122:39635
# 209.127.62.179:3128
# 64.42.179.228:4443
# 190.90.80.237:999
# 31.40.27.214:3128
# 103.9.206.186:10008
# 136.244.99.51:8888
# 85.112.193.37:8080
# 47.56.110.204:8989
# 123.30.154.171:7777
# 47.243.177.210:8088
# 116.203.28.43:80
# 114.156.77.107:8080
# 89.145.162.81:3128
# 186.121.235.222:8080
# 64.225.4.17:10005
# 64.225.4.81:10005
# 89.117.32.209:80
# 207.2.120.19:80
# 152.70.192.41:80
# 134.195.101.34:8080
# 12.186.205.123:80
# 188.166.17.18:8881
# 20.157.194.61:80
# 43.157.10.238:8888
# 41.65.236.43:1981
# 50.174.7.156:80
# 50.174.7.154:80
# 80.228.235.6:80
# 20.206.106.192:80
# 50.239.72.17:80
# 50.174.7.157:80
# 50.168.210.226:80
# 50.168.49.106:80
# 50.239.72.16:80
# 50.235.240.86:80
# 185.140.53.137:80
# 50.220.168.134:80
# 50.168.49.111:80
# 50.239.72.19:80
# 50.174.145.8:80
# 207.34.88.177:80
# 157.245.97.60:80
# 107.1.93.211:80
# 50.171.32.226:80
# 50.202.75.26:80
# 181.212.58.68:80
# 50.230.222.202:80
# 50.231.172.74:80
# 85.26.146.169:80
# 50.206.111.89:80
# 50.174.7.159:80
# 50.231.110.26:80
# 127.0.0.7:80
# 50.231.104.58:80
# 50.168.49.105:80
# 50.168.210.232:80
# 50.168.210.234:80
# 50.172.75.126:80
# 50.168.72.117:80
# 213.157.6.50:80
# 50.170.90.28:80
# 50.170.90.25:80
# 50.168.49.110:80
# 190.103.177.131:80
# 50.218.57.65:80
# 50.174.145.9:80
# 133.18.234.13:80
# 50.239.72.18:80
# 50.204.219.228:80
# 50.200.12.87:80
# 190.58.248.86:80
# 50.170.90.24:80
# 80.150.50.226:80
# 50.174.145.10:80
# 50.171.68.130:80
# 50.171.32.224:80
# 50.168.72.114:80
# 107.1.93.214:80
# 50.168.163.181:80
# 50.174.145.15:80
# 50.207.199.84:80
# 50.200.12.80:80
# 96.113.158.126:80
# 50.228.141.103:80
# 50.122.86.118:80
# 50.200.12.81:80
# 41.77.188.131:80
# 65.21.193.252:8080
# 109.236.44.181:8080
# 38.49.140.190:999
# 113.161.59.136:8080
# 202.154.19.163:8080
# 181.78.83.17:999
# 103.247.216.138:8080
# 50.228.141.99:80
# 107.1.93.218:80
# 172.105.103.135:3128
# 50.172.75.122:80
# 50.228.141.97:80
# 50.222.245.42:80
# 178.33.3.163:8080
# 50.221.166.2:80
# 50.174.7.153:80
# 50.206.111.88:80
# 136.243.90.203:80
# 107.1.93.215:80
# 50.171.32.228:80
# 50.172.75.124:80
# 50.174.145.14:80
# 50.171.32.222:80
# 50.218.57.68:80
# 50.218.57.74:80
# 50.218.57.64:80
# 50.168.49.108:80
# 50.204.219.229:80
# 50.200.12.85:80
# 50.171.32.225:80
# 50.222.245.40:80
# 50.228.141.102:80
# 50.170.90.26:80
# 80.120.130.231:80
# 50.168.72.118:80
# 50.218.57.67:80
# 50.227.121.37:80
# 50.227.121.39:80
# 50.227.121.33:80
# 62.141.11.68:80
# 50.227.121.36:80
# 50.228.141.101:80
# 50.200.12.83:80
# 77.48.244.78:80
# 4.175.121.88:80
# 50.171.32.229:80
# 50.228.141.100:80
# 50.168.163.166:80
# 32.223.6.94:80
# 50.218.57.70:80
# 91.92.155.207:3128
# 50.174.145.13:80
# 187.189.138.47:8888
# 110.78.28.94:8080
# 190.110.34.158:999
# 49.0.246.130:45554
# 71.86.129.131:8080
# 138.68.60.8:8080
# 20.24.43.214:80
# 20.210.113.32:80
# 186.121.235.66:8080
# 194.182.178.90:3128
# 34.82.224.175:33333
# 117.54.114.103:80
# 118.69.134.0:80
# 117.54.114.99:80
# 8.219.97.248:80
# 200.105.215.22:33630
# 103.127.1.130:80
# 8.213.129.20:2020
# 220.73.173.111:3001
# 75.89.101.62:80
# 117.54.114.100:80
# 12.186.205.121:80
# 115.96.208.124:8080
# 34.142.51.21:443
# 95.216.164.36:80
# 64.225.8.179:10005
# 190.63.35.30:9812
# 50.217.226.40:80
# 50.217.226.47:80
# 50.174.7.162:80
# 50.170.90.30:80
# 50.206.25.105:80
# 50.168.34.138:80
# 194.182.187.78:3128
# 50.217.226.43:80
# 20.205.61.143:80
# 50.217.226.42:80
# 50.168.163.180:80
# 50.171.152.30:80
# 50.174.7.158:80
# 41.207.187.178:80
# 50.217.226.44:80
# 50.217.226.41:80
# 50.174.7.152:80
# 50.174.7.155:80
# 50.168.163.177:80
# 50.207.199.80:80
# 202.180.21.203:8009
# 0.0.0.0:80
# 20.111.54.16:80
# 103.225.11.135:80
# 50.204.219.231:80
# 50.200.12.84:80
# 50.204.219.224:80
# """
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

#opens a csv file of proxies and prints out the ones that work with the url in the extract function

proxylist = []

with open('Bot\proxylist.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])

def extract(proxy):
    #this was for when we took a list into the function, without conc futures.
    #proxy = random.choice(proxylist)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:
        #change the url to https://httpbin.org/ip that doesnt block anything
        r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=2)
        print(r.json(), ' | Works')
    except:
        pass
    return proxy

with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract, proxylist)