from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Main, Dashboard
from .Details import GetProfileInfo
import json


def index(request):
    main = Main.objects.get(id=1)
    Usernames = Dashboard.objects.all().values()
    template = loader.get_template('Dashboard.html')
    from .Commands import Commands
    process = Commands()
    if request.method == 'POST' and 'startserver' in request.POST:
        if process.status == "Start":
            process.startserver()
            process.status = "Running"
        else:
            process.stopserver()
            process.status = "Start"

        return HttpResponseRedirect(reverse('index'))
    context = {
        'Main': main,
        'status': process.status,
        'ActivePlayers': Usernames,
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
    }
    return HttpResponse(template.render(context, request))


def output(request):
    from .Commands import Commands
    c = Commands()
    template = loader.get_template('console-output.html')
    output = []
    while c.process.poll() is None:
        print(c.process.stdout.readline())
        output.append(c.process.stdout.readline())
        context = {
            'output': output
        }
    return HttpResponse(template.render(context, request))
