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
    f = open("README.md","r")
    content = Markup(markdown.markdown(f.read()))
    return render_template('index.html', **locals())


@app.route('/times'
           '')
def times():
    scrapper_keys = cache.keys('Counter/Scrapper*Total')
    for key in scrapper_keys:
        country_retailer = re.findall(r'Counter/Scrapper(.*?)/Total', str(key))[0]
        count = int(cache.get(key))
        country_retailers[country_retailer] = count
    return jsonify(country_retailers)
