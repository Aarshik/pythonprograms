import urllib.request, urllib.parse, urllib.error
import json
address= 'http://py4e-data.dr-chuck.net/json?'
local= input('Enter Location: ')
url=address + urllib.parse.urlencode({"address": local,'key':42})
print('Retrieving', url)
fh=urllib.request.urlopen(url)
data=fh.read().decode()
print('Retrieved', len(data))
js=json.loads(data)
placeid= js['results'][0]['place_id']
print('The Place ID is: ', placeid)
