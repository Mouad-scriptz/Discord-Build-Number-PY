import requests as req
import re

def GetBN():
    client_request = req.get(f"https://discord.com/app", headers={"user-agent": "Mozilla/5.0"}).content.decode("utf-8") #getting the js names
    assetname = re.compile(r'([a-zA-z0-9]+)\.js', re.I).findall(client_request) #finding them
    asset = req.get(f"https://discord.com/assets/{assetname[len(assetname)-2]}.js", headers={"user-agent": "Mozilla/5.0"}).content.decode("utf-8") #getting the name before the last one and getting it
    string = re.compile('Build Number: [0-9]+, Version Hash: [A-Za-z0-9]+').findall(asset)[0].replace(' ', '').split(',') #finding build number
    return string[0].split(':')[1]
    
print(GetBN())
