#!/usr/bin/python
# -*- coding: utf-8 -*-

import apache_log_parser  
import glob  
import logging  
 
 #line_parser = apache_log_parser.make_parser("%h <<%P>> %t %Dus \"%r\" %>s %b  \"%{Referer}i\" \"%{User-Agent}i\" %l %u")
#line_parser2 = apache_log_parser.make_parser("%h <<%P>> %t %Dus \"%r\" %>s %b  \"%{Referer}i\" \"%{User-Agent}i\" %l %u")

#log_line_data = line_parser('127.0.0.1 <<6113>> [16/Aug/2013:15:45:34 +0000] 1966093us "GET / HTTP/1.1" 200 3478  "https://example.com/" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)" - -')
#pprint(log_line_data)

#log_line_data = line_parser('127.0.0.1 <<6113>> [16/Aug/2013:15:45:34 +0000] 1966093us "GET / HTTP/1.1" 200 3478  "https://example.com/" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)" - -')
#pprint(log_line_data)

# 91.177.59.121 
# [24/Oct/2016:00:01:02 -0700] 
# 0.265 
# https 
# www.udemy.com 
# "GET /staticx/udemy/js/webpack/fontawesome-webfont.2980083682e94d33a66eef2e7d612519.svg HTTP/1.1" 
# 200 
# 94289 
# "https://www.udemy.com/" 
# "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50"


# 91.177.59.121                          %h
# [24/Oct/2016:00:01:02 -0700]           '%t' 
# 0.265                                   '%D'
# https                                   '%H'
# www.udemy.com                              '%U' 
# "GET /staticx/udemy/js/webpack/fontawesome-webfont.2980083682e94d33a66eef2e7d612519.svg HTTP/1.1"  "%r\" 
# 200                                         '%s'  %>s 
# 94289                                        %b
# "https://www.udemy.com/" 
# "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50"  "%{User-Agent}i\" 


#line_parser = apache_log_parser.make_parser("%h <<%P>> %t %Dus \"%r\" %>s %b  \"%{Referer}i\" \"%{User-Agent}i\" %l %u")
#line_parser = apache_log_parser.make_parser("%h '%t' '%D' '%H' '%U' "%r" '%s' '%b' '%m'" )
line_parser = apache_log_parser.make_parser('%a %t %D') 

#log_line_data = line_parser('127.0.0.1 <<6113>> [16/Aug/2013:15:45:34 +0000] 1966093us "GET / HTTP/1.1" 200 3478  "https://example.com/" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)" - -')
log_line_data = line_parser('91.177.59.121 [24/Oct/2016:00:01:02 -0700] 0.265 https www.udemy.com "GET /staticx/udemy/js/webpack/fontawesome-webfont.2980083682e94d33a66eef2e7d612519.svg HTTP/1.1" 200 94289 "https://www.udemy.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50')

from pprint import pprint
pprint(log_line_data)
