#!/usr/bin/python
# -*- coding: utf-8 -*-

import optparse
import argparse
import sys
from collections import Counter

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

def udemy2(top):
# 8.       For each of the top 10 IPs, show the top 5 pages requested and the number of requests for each.
    # file   
    #udemy_logfile = r"C:\code\udemy\log1.txt"
    udemy_logfile = r"C:\code\udemy\sre_test_log.txt"   
    logfile = open(udemy_logfile, 'r')
    log = logfile.readlines()
    logfile.close()

    mytop = int(top)

    # 8.       For each of the top 10 IPs, show the top 5 pages requested and the number of requests for each.
    global p8
    for linea in log: 
        udemy_ip = linea.split()[0]      
        if udemy_ip not in dict_ips:
            dict_ips[udemy_ip] = 1
        else:
            value = dict_ips[udemy_ip] 
            # print (value)
            dict_ips[udemy_ip] = value+1
            # print(dict_ips[udemy_ip])
        p8 += 1
        
    print("################################################")
    print("################################################")
    
    # Printo top 10
    cnt = Counter(dict_ips)
    # print(cnt)
    cnt.most_common()
    for ip, times in cnt.most_common(mytop):
        print('The Ip: %s: Number of Requests: %s' % (ip, times))

        for linea2 in log:
            udemy_ip = linea2.split()[0]
            udemy_url = linea2.split(' ')[6]
            if udemy_ip == ip:        
                if udemy_url not in dict_ip_url:
                    dict_ip_url[udemy_url] = 1   
                else:
                    value = dict_ip_url[udemy_url] 
                    dict_ip_url[udemy_url] = value+1
                                  
        cnt2 = Counter(dict_ip_url)
        # print(cnt)
        cnt2.most_common()
        for url, times in cnt2.most_common(3):
            print('    The url: %s: is accesing %s ' % (url, times))
            # print('The URL: %s: Number of Requests: %s' % (url, times)
    print("################################################")
    print("################################################")

    return()


def main():

	"""Runs program and handles command line options"""
	p = optparse.OptionParser(description='--top-ips <Number>The top <Number> of IP addresses by request count.')

	p.add_option('-t','--topips',  default="1")

	options, arguments = p.parse_args()

	if options.topips:
		udemy2(options.topips)


if __name__ == '__main__':
	main()