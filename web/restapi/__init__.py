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
from datetime import timedelta
import pickle

app = Flask(__name__)

cache = redis.StrictRedis(
    host = "10.148.0.4",
    port = "6379",
)


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
    country_retailers_pickle_path = '/home/booneng/prometheus_exporter/country_retailers.p'    
    try:
        country_retailers = pickle.load(open(country_retailers_pickle_path, "rb"))
    except (OSError, IOError) as e:
        country_retailers = {}
    data = []
    for cr_key in country_retailers:
        country_retailer = country_retailers[cr_key]
        start_time = country_retailer['start_time']
        stop_time = country_retailer['stop_time']
        cr_data = {}   
        cr_data['key'] = cr_key
        cr_data['date'] = str(start_time.date())
        cr_data['start_time'] = str(start_time.time())
        if stop_time:
            cr_data['stop_time'] = str(stop_time.time())
            cr_data['duration'] = str(stop_time - start_time)
        data.append(cr_data)
    print(data)
    return render_template('index.html', **locals())
