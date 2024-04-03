from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Main, Dashboard
from .Details import GetProfileInfo
import json


def index(request):
    main = Main.objects.all().values()
    Usernames = Dashboard.objects.all().values()
    template = loader.get_template('Dashboard.html')
    context = {
        'Main': main,
        'ActivePlayers': Usernames
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    playerdata = GetProfileInfo(Dashboard.objects.get(id=id).username)
    print(Dashboard.objects.get(id=id).username)
    data = json.loads(playerdata.text)
    servername = Main.objects.all().values()
    template = loader.get_template('Details.html')
    context = {
        'servername': servername,
        'Player': data['data']['player']['username'],
        'Data': data['data']['player']['avatar'],
        'skin': data['data']['player']['skin_texture'],
        'status': ,
    }
    return HttpResponse(template.render(context, request))
