from random import randint
import re
from flask import Markup
import markdown
import redis
import datetime

cache = redis.StrictRedis(
    host = "10.148.0.4",
    port = "6379",
)
country_retailers_pickle_path = '/home/booneng/prometheus_exporter/country_retailers.p'
try:
    country_retailers = pickle.load(open(country_retailers_pickle_path, "rb"))
except (OSError, IOError) as e:
    country_retailers = {}
    
while True: 
    scrapper_keys = cache.keys('Counter/Scrapper*Total')
    for key in scrapper_keys:
        data = {}
        country_retailer = re.findall(r'Counter/Scrapper(.*?)/Total', str(key))[0]
        count = int(cache.get(key))
        current_time = datetime.datetime.now()
        data['count'] = count
        if country_retailer not in country_retailers:
            data['start_time'] = current_time
            data['count'] = count
            data['stop_time'] = None
            country_retailers[country_retailer] = data
            continue
        old_data = country_retailers[country_retailer]
        old_count = old_data['count']
        old_start_time = old_data['start_time']
        old_stop_time = old_data['stop_time']
        if count < old_count:
            data['start_time'] = current_time
            data['stop_time'] = None
        elif old_stop_time == None:
            if count == old_count:
                data['start_time'] = old_start_time
                data['stop_time'] = current_time
        country_retailers[country_retailer] = data
    pickle.dump(country_retailers, open(country_retailers_pickle_path, "wb" ))  
    time.sleep(20)