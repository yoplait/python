#!/usr/bin/python
# -*- coding: utf-8 -*-

import apache_log_parser  
import glob  
import logging  
 

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




# supported log file formats  
# APACHE_COMBINED="%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\""  
# APACHE_COMMON="%h %l %u %t \"%r\" %>s %b"  
 
APACHE_COMBINED="%h '%t' '%D' '%H' '%U' "%r" '%s' '%b' '%m'"  




def gulp(log_file_path, pattern=APACHE_COMBINED):  
 """ import and parse log files """  
 log_data=[]  
 line_parser=apache_log_parser.make_parser(pattern)  
 for file_name in glob.glob(log_file_path):  
   logging.info("file_name: %s" % file_name)  
   file = open(file_name, 'r')  
   lines = file.readlines()  
   file.close()  
   logging.info(" read %s lines" % len(lines))  
   for line in lines:  
     line_data=line_parser(line)  
     log_data.append(line_data)  
 logging.info("total number of events parsed: %s" % len(log_data))  
 return log_data  


gulp('C:\code\udemy\log1.txt')