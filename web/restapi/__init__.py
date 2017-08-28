from flask import Flask
from flask import request
from json import dumps,loads
from random import randint
from flask import jsonify
import re
from flask import Markup
import markdown
from flask import render_template
import redis
import datetime

app = Flask(__name__)

cache = redis.StrictRedis(
    host = "10.148.0.4",
    port = "6379",
)

country_retailers = {}

def help_decorator(f):
    """
    Returns the function info
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "/help" in request.path:
            return f.__doc__
        return f(*args, **kwargs)
    return decorated_function

app.debug = True

@app.route('/')
def index():
    #f = open("README.md","r")
    #content = Markup(markdown.markdown(f.read()))
    country_retailers = {'hi':'hi'}
    return render_template('index.html', **locals())


@app.route('/times'
           '')
def times():
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
        
        for country_retailer in country_retailers:
            pass
    return jsonify(country_retailers)
