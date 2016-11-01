#!/usr/bin/python
# -*- coding: utf-8 -*-

import optparse
import argparse
import sys
from collections import Counter
import operator

#Global variables
dict_ips = dict()   
dict_url = dict()   
dict_url_unsuc = dict()
dict_con_min = dict()
dict_ip_url = dict()

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0
p7 = 0
p8 = 0
p9 = 0
cnt = 0

################################################################################################################################################
################################################################################################################################################
 
    
def udemy6(top):
    # file   
    #udemy_logfile = r"C:\code\udemy\log.txt"
    #udemy_logfile = r"C:\code\udemy\log.txt"
    udemy_logfile = r"C:\code\udemy\sre_test_log.txt"   
    logfile = open(udemy_logfile, 'r')
    log = logfile.readlines()
    logfile.close()
    global p7
    number_successful = 0
    

    # necesito la ip de la coleccion
    global p2
    cnt = Counter(dict_ips)
    cnt.most_common()
    for ip, times in cnt.most_common(3):
        print('The Ip: %s: Number of Requests: %s' % (ip, times))
        print(ip)
        # obj = IPWhois(get_ip(ip))
        obj = IPWhois(ip)
        results = obj.lookup()
        print(results)
        # results = obj.get_host()
        # print(res["nets"][0]['country']])
        print("Country")
        print(results['nets'][0]['description'])
        #print("Abuse")
        #print(results["nets"][0]['abuse_emails'])
        p2 += 1
        
    print("################################################")
    print("################################################")
    return()


def main():

	"""Runs program and handles command line options"""
	p = optparse.OptionParser(description='--top-sources <Number> Lists the top <Number> IP owners based on the whois information. \
        Information about WHOIS: https://en.wikipedia.org/wiki/WHOIS This either can be source AS numbers or the name of the owner. ')

	p.add_option('-x','--topsources',  default="")

	options, arguments = p.parse_args()

	if options.topsources:
		udemy6(options.topsources)


if __name__ == '__main__':
	main()