#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#                 $$\                                   
#                 $$ |                                  
# $$\   $$\  $$$$$$$ | $$$$$$\  $$$$$$\$$$$\  $$\   $$\ 
# $$ |  $$ |$$  __$$ |$$  __$$\ $$  _$$  _$$\ $$ |  $$ |
# $$ |  $$ |$$ /  $$ |$$$$$$$$ |$$ / $$ / $$ |$$ |  $$ |
# $$ |  $$ |$$ |  $$ |$$   ____|$$ | $$ | $$ |$$ |  $$ |
# \$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$ | $$ | $$ |\$$$$$$$ |
#  \______/  \_______| \_______|\__| \__| \__| \____$$ |
#                                             $$\   $$ |
#                                             \$$$$$$  |
#                                              \______/ 
#    
# Juan Carlos Perez
# perezpardojc@gmail.com
# Senior SRE Coding Challenge
#

# Import section

import sys
import optparse
import argparse
from collections import Counter
import operator
import socket
from pprint import pprint
from collections import Counter
import time
import apache_log_parser
from ipwhois import IPWhois
import whois

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

def udemy3(request):

    # file   
    #udemy_logfile = r"C:\code\udemy\log.txt"
    #udemy_logfile = r"C:\code\udemy\log.txt"
    udemy_logfile = r"C:\code\udemy\sre_test_log.txt"   
    logfile = open(udemy_logfile, 'r')
    log = logfile.readlines()
    logfile.close()
    global p7
    number_successful = 0
    
    for linea in log:
        #print("########")
        #print("Pasada numero %i" %(p7))
        #print(linea)

        start=linea.index('[')
        end=linea.index(']')
        #print(start)
        #print(end)
        cadena = linea[ (start + 1) : start + (end-start)]
        #s = linea[ (start+1) : start + (end-start)]
        #s = s[(print linea.index('[')) : (print linea.index(']')) + ((print linea.index(']') - (print linea.index('[')))]
        #print(cadena)

        #time '[21/Mar/2011:17:32:42'
        #cadena = '21/Mar/2011:17:32:42'
        #print(cadena)
        date = cadena.split('/')
        #print(date)
        #print(date[0]) #day
        #print(date[1]) #month
        #print(date[2]) #time 


        #time '[21/Mar/2011:17:32:42'        
        #hour '17'
        hour = date[2].split(':')[1]
        #minutes '32'
        minute = date[2].split(':')[2]

        #problem with same minutes in several hours
        soda = hour + minute
        
        if soda not in dict_con_min:
            number_successful += 1
            #print("  %s No Esta en el Dictionary, es aniadida" %(soda) )
            dict_con_min[soda] = 1
        else:
            #print("  %s Esta en el Dictionary, se suma una ocurrencia" %(soda) )
            value = dict_con_min[soda]                   
            # print (value)
            dict_con_min[soda] = value+1
            # print(dict_ips[udemy_ip])
        p7 += 1

    #print(dict_con_min)

    print("Request count per minute")

    #for i in dict_con_min:
    #  print i, dict_con_min[i]

    for k, v in dict_con_min.iteritems():
        print k, v

    print("###########################################################")    
    print("Busiest time:", max(dict_con_min, key=dict_con_min.get))
    print("Petitions per minute:", dict_con_min[   max(dict_con_min, key=dict_con_min.get)] )
    print("###########################################################")    

    return()

def udemy4(starttime):

    # file   
    udemy_logfile = r"C:\code\udemy\log.txt"
    #udemy_logfile = r"C:\code\udemy\log1.txt"
    #udemy_logfile = r"C:\code\udemy\sre_test_log.txt"   
    logfile = open(udemy_logfile, 'r')
    log = logfile.readlines()
    logfile.close()
    global p7
    number_successful = 0

    print (starttime)
    myhour = starttime.split(':')[0]
    myminute= starttime.split(':')[1]
    print (myhour)
    print (myminute)

    for linea in log:



        #print("########")
        #print("Pasada numero %i" %(p7))
        #print(linea)

        start=linea.index('[')
        end=linea.index(']')
        #print(start)
        #print(end)
        cadena = linea[ (start + 1) : start + (end-start)]
        #s = linea[ (start+1) : start + (end-start)]
        #s = s[(print linea.index('[')) : (print linea.index(']')) + ((print linea.index(']') - (print linea.index('[')))]
        #print(cadena)

        #time '[21/Mar/2011:17:32:42'
        #cadena = '21/Mar/2011:17:32:42'
        #print(cadena)
        date = cadena.split('/')
        #print(date)
        #print(date[0]) #day
        #print(date[1]) #month
        #print(date[2]) #time 


        #time '[21/Mar/2011:17:32:42'        
        #hour '17'
        hour = date[2].split(':')[1]
        #minutes '32'
        minute = date[2].split(':')[2]


        if (hour >= myhour and minute >= myminute):
            print(linea)


    return()


def udemy5(endtime):

    # file   
    #udemy_logfile = r"C:\code\udemy\log.txt"
    #udemy_logfile = r"C:\code\udemy\log.txt"
    udemy_logfile = r"C:\code\udemy\sre_test_log.txt"   
    logfile = open(udemy_logfile, 'r')
    log = logfile.readlines()
    logfile.close()
    global p7
    number_successful = 0
    

    print (endtime)
    myhour = endtime.split(':')[0]
    myminute= endtime.split(':')[1]
    print (myhour)
    print (myminute)


    for linea in log:
    
        start=linea.index('[')
        end=linea.index(']')
        #print(start)
        #print(end)
        cadena = linea[ (start + 1) : start + (end-start)]
        #s = linea[ (start+1) : start + (end-start)]
        #s = s[(print linea.index('[')) : (print linea.index(']')) + ((print linea.index(']') - (print linea.index('[')))]
        #print(cadena)

        #time '[21/Mar/2011:17:32:42'
        #cadena = '21/Mar/2011:17:32:42'
        #print(cadena)
        date = cadena.split('/')
        #print(date)
        #print(date[0]) #day
        #print(date[1]) #month
        #print(date[2]) #time 


        #time '[21/Mar/2011:17:32:42'        
        #hour '17'
        hour = date[2].split(':')[1]
        #minutes '32'
        minute = date[2].split(':')[2]


        if (hour <= myhour and minute <= myminute):
            print(linea)

        p7 += 1

    return()    

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
    p = optparse.OptionParser(description='--ip=<IP address> or --ip=<IP range> Output log lines which matches either the <IP address> or the <IP range>. \
    The <IP range> format is in CIDR, e.g. 192.168.1.0/24. More about the format https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation')

    p.add_option('-i', '--ip', default="", help='returns verbose output')
    p.add_option('-t', '--topips', default="", help='returns verbose output')
    p.add_option('-r', '--requestrate', default="", help='returns verbose output')
    p.add_option('-s','--start',  default="")
    p.add_option('-e','--end',  default="")
    p.add_option('-x','--topsources',  default="")

    options, arguments = p.parse_args()

    if options.ip:        udemy1(options.ip)
    if options.topips:        udemy2(options.topips)
    if options.requestrate:        udemy3(options.requestrate)
    if options.start:        udemy4(options.start)
    if options.end:        udemy5(options.end)
    if options.topsources:        udemy6(options.topsources)


if __name__ == '__main__':
	main()