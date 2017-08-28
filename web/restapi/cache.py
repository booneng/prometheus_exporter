from flask_cache import Cache
from .Connectors import elastic
from .Connectors.repackage import repackFilters,repackHist
from json import loads
from flask import jsonify
#from json import dumps
from rapidjson import dumps
from flask import Response
from colormap import rgb2hex
import logging
from random import randint
import numpy as np
import re

cache = Cache()
@cache.memoize(timeout=3600)
def getAggs(filters={}):
    r = elastic.getAggs(filters=filters)
    r = repackFilters(r)
    return  Response(response=dumps(r), status=200, mimetype="application/json")#jsonify(r)

@cache.memoize(timeout=3600)
def colour(group=False, filters = {} , groupby = {}):
    field = 'ColourGroup' if group else 'Colour'
    r = elastic.getColorHist(filters=filters, groupby=groupby, field=field)
    r = elastic.repackColorHist(r)
    return  Response(response=dumps(r), status=200, mimetype="application/json")

g_trends = [ {"name":"Bomber Jacket","gender":"Female","change":20,"image": "http://lp2.hm.com/hmprod?set=source[/environment/2016/8AZ_0095_002R.jpg],width[3789],height[4431],x[792],y[90],type[FASHION_FRONT]&hmver=0&call=url[file:/product/main]"},
             {"name":"Mini Skirts","gender":"Female","change":45,"image":"http://static.my.zalora.net/p/something-borrowed-5177-6366521-1.jpg"},
             {"name":"Sports Leggings","gender":"Female","change":-45,"image":"http://www.forever21.com/images/1_front_750/00098304-01.jpg"},
             {"name":"Tote Bags","gender":"Female","change":-17,"image":"http://static.my.zalora.net/p/playboy-bunny-8043-8358421-1.jpg"},
             {"name":"Hem Jeans","gender":"Female","change":57,"image": "http://static.my.zalora.net/p/eyescream-5439-5131621-1.jpg"},
             {"name":"Off Shoulder Tops","gender":"Female","change":32,"image": "http://static.my.zalora.net/p/something-borrowed-9327-6641421-1.jpg"},
             {"name":"Mules","gender":"Female","change":26,"image":"http://cottonon.com/on/demandware.static/-/Sites-cog-rubishoes-master/default/dw8eb4bb9e/418168/418168-76-2.jpg"},
             {"name":"Sliders","gender":"Female","change":-2,"image":"http://images.asos-media.com/products/river-island-embroidered-sliders/8087991-1-brights?wid=2000&fit=constrain"},
             {"name":"Off Shoulder Dresses","gender":"Female","change":42,"image": "http://images.asos-media.com/products/asos-off-shoulder-mini-dress/8252671-1-yellow?wid=2000&fit=constrain"},
             {"name":"Wide Leg Trousers","gender":"Female","change":-12, "image":"http://static.my.zalora.net/p/topshop-1568-1832121-1.jpg"},
             {"name":"Horizontal Stripes","gender":"Female","change":41,"image":"http://static.my.zalora.net/p/zalora-0066-1134121-1.jpg"},
             {"name":"Pleated Skirts","gender":"Female","change":12,"image":"http://img.shein.com/images/shein.com/201704/32/14922356513344189155.jpg"}]


g_trendslookup = { i["name"]:i for i in g_trends}
@cache.memoize(timeout=3600)
def trends(filters={}):
    out = []
    for j in g_trends:
        change = j.get("change",1)
        if change <0:
            change = 0 
        np.random.seed(change)
        tmp = j
        tmp["index chart"] = {}
        tmp["index chart"]["score"] = list(np.random.normal(20,10,120))
        tmp["index chart"]["x-axis"] = [i for i in range(0,120)]
        out.append(tmp)
    logging.warning(out)
    return Response(response=dumps(out), status=200, mimetype="application/json")

@cache.memoize(timeout=3600)
def trenddetails(trend="Bomber Jacket",filters={}):
    if not trend:
        trend = "Bomber Jacket"
    trendinfo = g_trendslookup.get(trend,{})
    change = trendinfo.get("change",1)
    change = abs(change)
    np.random.seed(change)    
    counts =  list(int(i) for i in np.random.randint(8000,13000,2))
    counts.sort()
    trendinfo["product count"] = counts[0]
    trendinfo["option count"] = counts[1]
    np.random.seed(change)    
    trendinfo["index chart"] = {}
    trendinfo["index chart"]["score"] = list(np.random.normal(20,10,120))
    trendinfo["index chart"]["x-axis"] = [i for i in range(0,120)]    
    trendinfo["activity chart"] = {}
    np.random.seed(change)
    trendinfo["activity chart"]["Out of Stock"] = [int(i) for i in np.random.randint(0,100,120)]
    np.random.seed(change+1)
    trendinfo["activity chart"]["In Stock"] = [int(i) for i in np.random.randint(0,100,120)]
    trendinfo["activity chart"]["x-axis"] = [i for i in range(0,120)]
    np.random.seed(change) 
    bscores = list(int(i) for i in np.random.randint(500,5000,5))
    bscores.sort(reverse=True)
    brands = ["ASOS","SheIn","ZALORA","Something Borrowed","Forever 21"]
    trendinfo["brands"] = [{"name":brands[i],"count":bscores[i]} for i in range(5)]
    np.random.seed(change) 
    rscores = list(int(i) for i in np.random.randint(1000,10000,5))
    rscores.sort(reverse=True)
    retailers = ["ASOS (UK)","Boohoo (UK)","ZALORA (MY)","Cotton On (MY)","Mango (MY)"]
    trendinfo["retailers"] = [{"name":retailers[i],"count":rscores[i]} for i in range(5)]
    trendinfo["details"] = "{} has been a growing in popularty across 2017 and has seen a particularly large increase in the last month particularly".format(trend)
    np.random.seed(change) 
    pricing =  list(int(i) for i in np.random.randint(30,500,3))
    pricing.sort()
    trendinfo["price stats"]=[{"name":"Min","count":pricing[0]},{"name":"Median","count":pricing[1]},{"name":"Max","count":pricing[2]}]
    np.random.seed(change+10)
    props =  list(i for i in np.random.random(2))
    m1 = int((counts[0]+counts[1])*props[0])
    m2 = (counts[0]+counts[1]) - m1
    d1 = int((counts[0]+counts[1])*props[1])
    d2 = (counts[0]+counts[1]) - d1
    
    markets = filters.get('Market', d=[])
    trendinfo["markets"] = [{"name":"UK","count":m1},{"name":"MY","count":m2} ] 
    trendinfo["discounts"] = [ {"name":"Discounted", "count":d1},{"name":"Full Price","count":d2}]    
    return Response(response=dumps(trendinfo), status=200, mimetype="application/json")
    