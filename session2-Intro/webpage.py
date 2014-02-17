import urllib2
from BeautifulSoup import *

f = urllib2.urlopen('http://www.python.org/')
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
