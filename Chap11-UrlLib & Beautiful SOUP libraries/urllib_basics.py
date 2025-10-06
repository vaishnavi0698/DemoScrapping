"""
import urllib.request, urllib.parse, urllib.error
import string

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

"""
import urllib.request

url = 'http://data.pr4e.org/romeo.txt'
uhandle = urllib.request.urlopen(url) # opens the given web URL and returns a file-like object
text = uhandle.read().decode()       # read() will read the bytes inside file like object and decode() will convert the bytes into string format.
print(text)

