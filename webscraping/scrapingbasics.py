
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("enter the webpage url: ")
html = urllib.request.urlopen(url).read()
print(html)
soup = BeautifulSoup(html, 'html.parser')
