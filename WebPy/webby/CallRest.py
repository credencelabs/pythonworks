'''
Created on Oct 5, 2020

@author: SUNDAR
'''
from urllib import request, parse

# Base URL being accessed
url = 'http://gopraniot.com/devices/devres/EC101'
u = request.urlopen(url)
resp = u.read()
print(resp)