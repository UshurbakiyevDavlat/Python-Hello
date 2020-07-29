# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


tags = soup('a')
dictin=list()



count=int(input("count:"))
position=int(input("position:"))
names=url
ctr=0
while count+1>0:
    ctr=0
    print(url)
    for tag in tags:
        url=(tag.get('href', None))
        ctr+=1
        if ctr==position:
            break


    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    count-=1
