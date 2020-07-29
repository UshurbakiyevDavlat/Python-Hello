import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
ctr=0
sum=0
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url =  parms['address']
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')


    tree = ET.fromstring(data)
    counts= tree.findall('comments/comment')

    print('Count:',len(counts))

    for item in counts:
        sum+=int(item.find('count').text)

    print('Sum:',sum)
