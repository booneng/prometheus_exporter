from flask import Flask
from flask import request
from .Connectors import elastic
app = Flask(__name__)
from json import dumps,loads
from random import randint
from flask import jsonify
import re
from flask import Markup
from functools import wraps
import markdown
from flask import render_template

app.config['CACHE_TYPE'] = 'simple'
cache.init_app(app)
#cache = Cache(app,config={'CACHE_TYPE': 'simple'})
#from rapidjson import dumps,loads

@app.route('/')
def index():
    f = open("README.md","r")
    content = Markup(markdown.markdown(f.read()))
    return render_template('index.html', **locals())

