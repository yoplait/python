#!/usr/bin/python
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import os.path
import sys
import re
import apache_log_parser
from pprint import pprint


# 91.177.59.121 [24/Oct/2016:00:01:02 -0700] 0.265 https www.udemy.com 
# "GET /staticx/udemy/js/webpack/fontawesome-webfont.2980083682e94d33a66eef2e7d612519.svg HTTP/1.1" 
# 200 94289 "https://www.udemy.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50"

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


# file url
theFile = open('C:\code\udemy\log1.txt','r')

#print theFile
FILE = theFile.readlines()
theFile.close()

loglist = []

for line in FILE:
	print line    
	myline = line.strip()
	tmp = myline.split(' ')

	log_ip = tmp[0]

	log_date = tmp[1]
	log_time_loaded = tmp[2]

	log_protocol = tmp[3]
	log_domain = tmp[4]
	log_petition = tmp[5]

	log_code = tmp[6]
	log_bytes = tmp[6]
	log_url = tmp[7]

	log_agent = tmp[8]


	print "IP", log_ip
	print "Time", log_date
	print "Time to load", log_time_loaded
	print "Protocol", log_protocol
	print "Domain", log_domain
	print "Petition", log_petition
	print "Code", log_code
	print "Size", log_bytes
	print "URL", log_url
	print "Agent", log_agent


	#get the starting/ending indices of request & useragents by their quotes
	request_start = doublequotes[0]+1
	request_end = doublequotes[1]
	useragent_start = doublequotes[4]+1
	useragent_end = doublequotes[5]
	request = line[request_start:request_end]
	useragent = line[useragent_start:useragent_end]
