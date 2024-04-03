import json, urllib.request, requests

def GetProfileInfo(profilename):
    r = requests.get('https://playerdb.co/api/player/minecraft/' + str(profilename))
    print(r.json)
    return r
