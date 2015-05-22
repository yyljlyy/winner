# coding=utf-8
import json
from time import ctime
import sys
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from winner.models import UserProfile

__author__ = 'lee'

handler404 = 'winner.views.page_not_found'

# 主页跳转
def home(request):
    liste = UserProfile.objects.select_related()
    lists = UserProfile.objects.using('orcales').select_related()
    return render(request, 'index.html', {"list": liste, "lists": lists})

# 添加用户
def add_user(request):
    dict = {}
    info = '用户保存成功！'
    try:
        if request.method == 'GET':
            name = request.GET.get('name')
            age = request.GET.get('age')
            address = request.GET.get('address')
    except:
        info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
    UserProfile.objects.create(name=name, age=age, address=address) #model执行语句
    UserProfile.objects.using('orcales').create(name=name, age=age, address=address)
    dict['message'] = info
    dict['create_at'] = str(ctime())
    jsons = json.dumps(dict)
    return HttpResponse(jsons, content_type='application/json')

# MySQL删除用户
def delete_user(request):
    dict = {}
    info = '用户删除成功！'
    try:
        if request.method == 'GET':
            ids = request.GET.get('id')
    except:
        info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
    b = UserProfile.objects.get(id=ids)
    # b = UserProfile.objects.using('orcales').get(id=ids)
    b.delete()
    dict['message'] = info
    jsons = json.dumps(dict)
    return HttpResponse(jsons, content_type='application/json')

#Orcale删除用户
def delete_ouser(request):
    dict = {}
    info = '用户删除成功！'
    try:
        if request.method == 'GET':
            ids = request.GET.get('id')
    except:
        info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
    b = UserProfile.objects.using('orcales').get(id=ids)
    b.delete()
    dict['message'] = info
    jsons = json.dumps(dict)
    return HttpResponse(jsons, content_type='application/json')
#MySQL 更新用户
def update_user(request):
    dict = {}
    info = '用户更新成功！'
    try:
        if request.method == 'GET':
            ids = request.GET.get('id')
            name = request.GET.get('name')
            age = request.GET.get('age')
            address = request.GET.get('address')
    except:
        info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
    UserProfile.objects.filter(id=ids).update(name=name, age=age, address=address)
    dict['message'] = info
    jsons = json.dumps(dict)
    return HttpResponse(jsons, content_type='application/json')

# Orcale 更新用户
def update_ouser(request):
    dict = {}
    info = '用户更新成功！'
    try:
        if request.method == 'GET':
            ids = request.GET.get('id')
            name = request.GET.get('name')
            age = request.GET.get('age')
            address = request.GET.get('address')
    except:
        info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
    UserProfile.objects.using('orcales').filter(id=ids).update(name=name, age=age, address=address)
    dict['message'] = info
    jsons = json.dumps(dict)
    return HttpResponse(jsons, content_type='application/json')

def page_not_found(request):
    return render(request, "404.html")