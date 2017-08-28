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
import threading

#country_retailers_pickle_path = '/usr/src/app/web/static/country_retailers.p'

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
    data = [{'start_time': '10:08:34.111925', 'date': '2017-08-28', 'key': '/MY/urbanoutfitters'}, {'start_time': '10:08:33.405925', 'date': '2017-08-28', 'key': '/MY/whitesoot'}, {'start_time': '10:08:33.859899', 'date': '2017-08-28', 'key': '/MY/pinknproper'}, {'start_time': '10:08:34.313662', 'date': '2017-08-28', 'key': '/MY/doublewoot'}, {'start_time': '10:08:34.364051', 'date': '2017-08-28', 'key': '/MY/choies'}, {'start_time': '10:08:33.305004', 'date': '2017-08-28', 'key': '/MY/blaqmagiklvrs'}, {'start_time': '10:08:34.212819', 'date': '2017-08-28', 'key': '/MY/redsrevenge'}, {'start_time': '10:08:33.204097', 'date': '2017-08-28', 'key': '/MY/accessorize'}, {'start_time': '10:08:33.809455', 'date': '2017-08-28', 'key': '/MY/theeditorsmarket'}, {'start_time': '10:08:33.910350', 'date': '2017-08-28', 'key': '/MY/charlesandkeith'}, {'start_time': '10:08:32.346181', 'date': '2017-08-28', 'key': '/MY/zalora'}, {'start_time': '10:08:33.052718', 'date': '2017-08-28', 'key': '/MY/lululemon'}, {'start_time': '10:08:32.043310', 'date': '2017-08-28', 'key': '/MY/milktee'}, {'start_time': '10:08:34.162383', 'date': '2017-08-28', 'key': '/MY/majordrop'}, {'start_time': '10:08:34.518086', 'date': '2017-08-28', 'key': '/MY/riverisland'}, {'start_time': '10:08:32.295629', 'date': '2017-08-28', 'key': '/MY/poplook'}, {'start_time': '10:08:34.568543', 'date': '2017-08-28', 'key': '/MY/adidas'}, {'start_time': '10:08:33.103202', 'date': '2017-08-28', 'key': '/MY/uk_asos'}, {'start_time': '10:08:33.557218', 'date': '2017-08-28', 'key': '/MY/modcloth'}, {'start_time': '10:08:31.992853', 'date': '2017-08-28', 'key': '/MY/mdscollections'}, {'start_time': '10:08:34.414433', 'date': '2017-08-28', 'key': '/MY/christyng'}, {'start_time': '10:08:31.942286', 'date': '2017-08-28', 'key': '/MY/lookbookstore'}, {'start_time': '10:08:32.194706', 'date': '2017-08-28', 'key': '/MY/uniqlo'}, {'start_time': '10:08:34.061555', 'date': '2017-08-28', 'key': '/MY/dotti'}, {'start_time': '10:08:32.548025', 'date': '2017-08-28', 'key': '/MY/lipsy'}, {'start_time': '10:08:32.245145', 'date': '2017-08-28', 'key': '/MY/nastygal'}, {'start_time': '10:08:32.144262', 'date': '2017-08-28', 'key': '/MY/forever21'}, {'start_time': '10:08:34.464869', 'date': '2017-08-28', 'key': '/MY/fashionvalet'}, {'start_time': '10:08:33.254521', 'date': '2017-08-28', 'key': '/MY/pomelofashion'}, {'start_time': '10:08:34.263223', 'date': '2017-08-28', 'key': '/MY/showpo'}, {'start_time': '10:08:33.758985', 'date': '2017-08-28', 'key': '/MY/boohoo'}, {'start_time': '10:08:32.699306', 'date': '2017-08-28', 'key': '/MY/sephora'}, {'start_time': '10:08:32.901137', 'date': '2017-08-28', 'key': '/MY/twenty3'}, {'start_time': '10:08:33.607650', 'date': '2017-08-28', 'key': '/MY/shein'}, {'start_time': '10:08:32.497611', 'date': '2017-08-28', 'key': '/MY/hm'}, {'start_time': '10:08:32.447148', 'date': '2017-08-28', 'key': '/MY/dorothyperkins'}, {'start_time': '10:08:32.850699', 'date': '2017-08-28', 'key': '/MY/cottonon'}, {'start_time': '10:08:33.355455', 'date': '2017-08-28', 'key': '/MY/tuesdaycouture'}, {'start_time': '10:08:33.456390', 'date': '2017-08-28', 'key': '/MY/hermo'}, {'start_time': '10:08:32.648869', 'date': '2017-08-28', 'key': '/MY/lazada'}, {'start_time': '10:08:33.153653', 'date': '2017-08-28', 'key': '/MY/saboskirt'}, {'start_time': '10:08:32.749789', 'date': '2017-08-28', 'key': '/MY/missguided'}, {'start_time': '10:08:33.506829', 'date': '2017-08-28', 'key': '/MY/chichiclothing'}, {'start_time': '10:08:32.396684', 'date': '2017-08-28', 'key': '/MY/hookclothing'}, {'start_time': '10:08:32.800220', 'date': '2017-08-28', 'key': '/SG/lornajane'}, {'start_time': '10:08:32.093821', 'date': '2017-08-28', 'key': '/MY/keimag'}, {'start_time': '10:08:33.960838', 'date': '2017-08-28', 'key': '/MY/topshop'}, {'start_time': '10:08:32.598470', 'date': '2017-08-28', 'key': '/MY/ashbenimble'}, {'start_time': '10:08:33.658094', 'date': '2017-08-28', 'key': '/SG/zalora'}, {'start_time': '10:08:32.951583', 'date': '2017-08-28', 'key': '/MY/thetinselrack'}, {'start_time': '10:08:33.002239', 'date': '2017-08-28', 'key': '/MY/mango'}, {'start_time': '10:08:33.708476', 'date': '2017-08-28', 'key': '/MY/parsealed'}, {'start_time': '10:08:34.011193', 'date': '2017-08-28', 'key': '/MY/bagbeg'}]
    return render_template('index.html', **locals())


@app.route('/times'
           '')
def times():
    country_retailers = loads(cache.get('scrapper_time_metrics').decode('utf-8'))
    data = []
    for cr_key in country_retailers:
        country_retailer = country_retailers[cr_key]
        start_time = country_retailer['start_time']
        stop_time = country_retailer.get('stop_time', None)
        error = country_retailer.get('error', None)
        cr_data = {}   
        cr_data['key'] = cr_key
        cr_data['date'] = str(start_time.date())
        cr_data['start_time'] = str(start_time.time())
        if stop_time:
            cr_data['stop_time'] = str(stop_time.time())
            cr_data['duration'] = str(stop_time - start_time)
        if error:
            cr_data['duration'] = error
        data.append(cr_data)
    return render_template('index.html', **locals())
