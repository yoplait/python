#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import os.path
import sys
import re
import apache_log_parser
from pprint import pprint

class LogAnalyzer():
    """ Parses and summarizes nginx logfiles """

    def __init__(self, readfile, writefile, topcount=5):
        """ Initializing """
        self.summary = {
            "requests": {},
            "ips": {},
            "useragents": {}
        }

        self.topcount = topcount

        self.reafile = readfile
        self.writefile = writefile

    def analyze(self):
        """ Reads and splits the access-log into our dictionary """
        #is file?
        if not os.path.isfile(self.reafile):
            print(self.reafile, "does not exist! exiting")
            exit(1)

        log = open(self.reafile, 'r')
        lines = log.readlines()
        log.close()
        loglist = []

        for s in lines:
            line = s.strip()
            tmp = line.split(' ')
            ip = tmp[0]

            #not the finest way...get indices of double quotes
            doublequotes = LogAnalyzer.find_chars(line, '"')

            #get the starting/ending indices of request & useragents by their quotes
            request_start = doublequotes[0]+1
            request_end = doublequotes[1]
            useragent_start = doublequotes[4]+1
            useragent_end = doublequotes[5]

            request = line[request_start:request_end]
            useragent = line[useragent_start:useragent_end]

            #writing a dictionary per line into a list...huh...dunno
            loglist.append({
                "ip": ip,
                "request": request,
                "useragent": useragent
            })

        self.summarize(loglist)
        self.write_summary()

    def summarize(self, cols):
        """ count occurences """
        for col in cols:
            if not col['request'] in self.summary['requests']:
                self.summary['requests'][col['request']] = 0
            self.summary['requests'][col['request']] += 1

            if not col['ip'] in self.summary['ips']:
                self.summary['ips'][col['ip']] = 0
            self.summary['ips'][col['ip']] += 1

            if not col['useragent'] in self.summary['useragents']:
                self.summary['useragents'][col['useragent']] = 0
            self.summary['useragents'][col['useragent']] += 1

    def write_summary(self):
        """ sorts and writes occurences into file """
        summary = open(self.writefile, 'w')
        summary.write("Log summary\n")
        for key in self.summary:
            list = sorted(self.summary[key].items(), key=lambda x: x[1], reverse=True)
            list = list[:self.topcount]
            summary.write("\nTop "+key+":\n")
            for l in list:
                summary.write(l[0]+": "+str(l[1])+" times\n")
        summary.close()

    @staticmethod
    def find_chars(string, char):
        """ returns a list of all indices of char inside string """
        return [i for i, ltr in enumerate(string) if ltr == char]




if __name__ == '__main__':
	# file url
	theFile = open('C:\code\udemy\log.txt','r')
    logfile = 'C:\code\udemy\log.txt'

    summaryfile = './access_summary.log'
    summary = LogAnalyzer(logfile, summaryfile, 5)
    summary.analyze()

	line_parser = apache_log_parser.make_parser("%h <<%P>> %t %Dus \"%r\" %>s %b  \"%{Referer}i\" \"%{User-Agent}i\" %l %u")
	line_parser2 = apache_log_parser.make_parser("%h <<%P>> %t %Dus \"%r\" %>s %b  \"%{Referer}i\" \"%{User-Agent}i\" %l %u")


	log_line_data = line_parser('127.0.0.1 <<6113>> [16/Aug/2013:15:45:34 +0000] 1966093us "GET / HTTP/1.1" 200 3478  "https://example.com/" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)" - -')
	pprint(log_line_data)

	#print theFile
	FILE = theFile.readlines()
	theFile.close()
	loglist = []

	log_line_data = line_parser('127.0.0.1 <<6113>> [16/Aug/2013:15:45:34 +0000] 1966093us "GET / HTTP/1.1" 200 3478  "https://example.com/" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)" - -')
	pprint(log_line_data)


	# file url
	theFile = open('C:\code\udemy\log.txt','r')

	#print theFile
	FILE = theFile.readlines()
	theFile.close()
	loglist = []

	for line in FILE:
	    print line    
