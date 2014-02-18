'''
webpage.py - read a page parse it and print the text

'''
import urllib2
from BeautifulSoup import *
import sys

try:
	url = sys.argv[1]
except:
	url = 'http://www.python.org/'

f = urllib2.urlopen(url)
html = f.read()
soup = BeautifulSoup(html)
print soup

# retrieve all paras tags
tags = soup('p')
for tag in tags:
    print tag

# retrieve all links

tags = soup('a')
for tag in tags:
    print tag.get('href',None)
