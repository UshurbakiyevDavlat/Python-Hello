import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verife_mode=ssl.CERT_NONE

url=input('Enter location:')
print("Retrieving:",url)
uh=urllib.request.urlopen(url,context=ctx)

data=uh.read()
info = json.loads(data)
print('Retrieved',len(data),'characters')


ctr=0
sum=0
for item in info['comments']:


    sum+=int(item['count'])

print('Count:', len(info['comments']))

print('Sum',sum)
