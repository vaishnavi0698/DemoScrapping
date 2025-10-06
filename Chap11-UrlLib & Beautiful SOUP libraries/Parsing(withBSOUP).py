# basic web scraper using Python + BeautifulSoup!

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("enter the webpage url: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

