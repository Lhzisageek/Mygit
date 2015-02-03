from django.template.loader import get_template
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import Template,Context
import datetime
def hello(request):
    return HttpResponse("你好，谢文佩。")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>"%now
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body>In %s hour(s),it will be %s.</body></html>"%(offset,dt)
    return HttpResponse(html)

def static_html(request):
    now = datetime.datetime.now()
    fp = open('/Users/lihz/python/django/mysite/mysite/a.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'current_date':now}))
    return HttpResponse(html)

def my_html(request):
    t = get_template('a.html')
    now = datetime.datetime.now()
    html = t.render(Context())
    return HttpResponse(html)

def zhihu(request):
    t = get_template('zhihu.html')
    html = t.render(Context())
    return HttpResponse(html)
   
def worms(request):
    t = get_template('b.html')
    html = t.render(Context())
    return HttpResponse(html)

datas = [
    {"id":"1","name":"huawei"},
    {"id":"2","name":"young girl"},
    {"id":"3","name":"father"},
    {"id":"4","name":"son"},
    {"id":"5","name":"haha"},
    {"id":"6","name":"xiewenpei"},
    {"id":"7","name":"lihz"},
    {"id":"8","name":"python"},
]
def show(request):
    t = get_template('data.html')
    html = t.render(Context({'datas':datas}))
    return HttpResponse(html)
