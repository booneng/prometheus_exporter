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

app = Flask(__name__)

cache = redis.StrictRedis(
    host = "redis.shopprapp.io",
    port = "6379",
)

@app.route('/')
def index():
    f = open("README.md","r")
    content = Markup(markdown.markdown(f.read()))
    return render_template('index.html', **locals())


@app.route('/times')
def index():
    scrapper_keys = cache.keys('Counter/Scrapper*Total')
    for key in scrapper_keys:
        country_retailer = re.findall(r'Counter/Scrapper(.*?)/Total', str(key))[0]
        count = int(cache.get(key))
    return {}
