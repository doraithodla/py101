'''
webpage.py - read a page parse it and print the text

'''
import requests
from bs4 import BeautifulSoup
import sys

try:
    url = sys.argv[1]
except:
    url = 'http://www.python.org/'

f = requests.get(url)
html = f.content()
soup = BeautifulSoup(html)
print(soup)

# retrieve all paras tags
tags = soup('p')
for tag in tags:
    print(tag)

# retrieve all links

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
