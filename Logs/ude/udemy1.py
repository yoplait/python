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

def udemy1(ip):
    # file   
    #udemy_logfile = r"C:\code\udemy\log1.txt"
    udemy_logfile = r"C:\code\udemy\log.txt"

    logfile = open(udemy_logfile, 'r')
    log = logfile.readlines()
    logfile.close()
    print ("#########################################")
    print ("We are looking for the ip: ", ip)
    print ("#########################################")

    for linea in log:
	  	if (ip == linea.split()[0]):
			print linea

    global p1
    for linea in log: 
        # top_ten = sorted(dict_ips.keys(), key = len(dict_ips...))
        # variables
        # counter++
        print("########")
        print("Read entry %i" %(p1))
        udemy_ip = linea.split()[0]
        
        print(udemy_ip)
        
        if udemy_ip not in dict_ips:
            print("  %s Is not in dictionary, lets go to add" %(udemy_ip) )
            dict_ips[udemy_ip] = 1
        else:
            print("  %s Is in the dictionary, we add as another case" %(udemy_ip) )
            value = dict_ips[udemy_ip] 
            # print (value)
            dict_ips[udemy_ip] = value+1
        p1 += 1
        
    print("################################################")
    print("################################################")
    # Printo top 10
    cnt = Counter(dict_ips)
    print(cnt)
    cnt.most_common()
    for ip, times in cnt.most_common(3):
        print('The Ip: %s: Number of Requests: %s' % (ip, times))
    return linea.split()[0]


def main():

	"""Runs program and handles command line options"""
	p = optparse.OptionParser(description='--ip=<IP address> or --ip=<IP range> Output log lines which matches either the <IP address> or the <IP range>. \
	The <IP range> format is in CIDR, e.g. 192.168.1.0/24. More about the format https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation')

	p.add_option('-i','--ip',  default="")

	options, arguments = p.parse_args()

	if options.ip:
		udemy1(options.ip)


if __name__ == '__main__':
	main()