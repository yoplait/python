

# imports
import builtins
import sys
import socket
from ipwhois import IPWhois
from pprint import pprint
from asyncio.tasks import wait
from collections import Counter
import time
import apache_log_parser
import re

#line = '172.16.0.3 - - [25/Sep/2002:14:04:19 +0200] "GET / HTTP/1.1" 401 - "" "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020827"'
#regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'

#print re.match(regex, line).groups()

parts = [
    r'(?P<host>\S+)',                   # host %h
    r'\S+',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<referer>.*)"',               # referer "%{Referer}i"
    r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
]


pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
line = '172.16.0.3 - - [25/Sep/2002:14:04:19 +0200] "GET / HTTP/1.1" 401 - "" "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020827"'

m = pattern.match(line)
res = m.groupdict()

for key, value in res.iteritems() :
    print key, value

print '#################################################################'
print '#################################################################'

# 91.177.59.121                          %h   The ip
# [24/Oct/2016:00:01:02 -0700]           '%t' The time 
# 0.265                                   '%D' Time to load
# https                                   '%H'  protocol
# www.udemy.com                              '%U'  url 
# "GET /staticx/udemy/js/webpack/fontawesome-webfont.2980083682e94d33a66eef2e7d612519.svg HTTP/1.1"  "%r\"  petition
# 200                                         '%s'  %>s  code
# 94289                                        %b bytes
# "https://www.udemy.com/"    resource
# "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50"  "%{User-Agent}i\"  user agent

parts2 = [
    r'(?P<host>\S+)',                   # host %h
    r'\[(?P<time>.+)\]',                # time %t
	r'(?P<timing>\S+)',                 # timing	
    r'(?P<protocol>\S+)',               # protocol
    r'(?P<url>\S+)',                    # url
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<referer>.*)"',               # referer "%{Referer}i"
    r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
]


pattern2 = re.compile(r'\s+'.join(parts2)+r'\s*\Z')
line2 = '91.177.59.121 [24/Oct/2016:00:01:02 -0700] 0.265 https www.udemy.com "GET /staticx/udemy/js/webpack/fontawesome-webfont.2980083682e94d33a66eef2e7d612519.svg HTTP/1.1" 200 94289 "https://www.udemy.com/"  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50"' 

m2 = pattern2.match(line2)
res2 = m2.groupdict()


for key, value in res2.iteritems() :
    print key, value




if res["user"] == "-":
    res["user"] = None

res["status"] = int(res["status"])

if res["size"] == "-":
    res["size"] = 0
else:
    res["size"] = int(res["size"])

if res["referer"] == "-":
    res["referer"] = None