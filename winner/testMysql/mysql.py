import json
import sys
from time import ctime
from django.http import HttpResponse
from winner.models import UserProfile

__author__ = 'lee'


def newName(request):
    dict = {}
    info = 'Data log save success'
    print request.method
    print request.GET
    print request.GET.QueryDict
    try:
        if request.method == 'GET':
            req = json.loads(request.GET)
            name = req['name']
            print name
            age = req['age']
            print age
            address = req['address']
            print address
    except:
        info = "%s || %s" % (sys.exc_info()[0], sys.exc_info()[1])
    UserProfile.objects.create(name=name, age=age, address=address)
    dict['message'] = info
    dict['create_at'] = str(ctime())
    jsons = json.dumps(dict)
    return HttpResponse(jsons)