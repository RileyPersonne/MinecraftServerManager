import json, urllib.request, requests

def GetProfileInfo(profilename):
    r = requests.get('https://playerdb.co/api/player/minecraft/stellarum4749')
    print(r.json)
    return r
