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
import socket
from pprint import pprint
from collections import Counter
import time
import apache_log_parser
from ipwhois import IPWhois
import whois
#from asyncio.tasks import wait
#import builtins


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

def get_ip(log):
    global p1
    for linea in log: 
        # top_ten = sorted(dict_ips.keys(), key = len(dict_ips...))
        # variables
        # counter++
        print("########")
        print("Read number %i" %(p1))
        udemy_ip = linea.split()[0]
        print(udemy_ip)      
        print(udemy_ip)
        
        if udemy_ip not in dict_ips:
            print("  %s No Esta en el Dictionary, es aniadida" %(udemy_ip) )
            dict_ips[udemy_ip] = 1
        else:
            print("  %s Esta en el Dictionary, se suma una ocurrencia" %(udemy_ip) )
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

  
def get_top10_top5url(log, log2):
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
    for ip, times in cnt.most_common(3):
        print('The Ip: %s: Number of Requests: %s' % (ip, times))

        for linea2 in log2:             
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
    return()


def get_request_per_minute(log):
# 7.       The total number of requests made every minute in the time period covered.
# so we need to look to the minutes and add one conection each line per that time
    global p7
    number_successful = 0
    
    for linea in log:
        print("########")
        print("Pasada numero %i" %(p7))
                
        #time '[21/Mar/2011:17:32:42'
        date = linea.split(' ')[3]
        #hour '17'
        hour = date.split(':')[1]
        #minutes '32'
        minute = date.split(':')[2]

        #problem with same minutes in several hours
        soda = hour + minute
        
        if soda not in dict_con_min:
            number_successful += 1
            print("  %s No Esta en el Dictionary, es aniadida" %(soda) )
            dict_con_min[soda] = 1
        else:
            print("  %s Esta en el Dictionary, se suma una ocurrencia" %(soda) )
            value = dict_con_min[soda]                   
            # print (value)
            dict_con_min[soda] = value+1
            # print(dict_ips[udemy_ip])
        
        p7 += 1
        return()
    
    
    
def get_owner_ip(log):
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
        # print(results)
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
# return results


################################################################################################################################################################
################################################################################################################################################################

def main():
    # file   
    #udemy_logfile = r"C:\code\udemy\log1.txt"
    udemy_logfile = r"C:\code\udemy\log.txt"

    logfile = open(udemy_logfile, 'r')
    log = logfile.readlines()
    logfile.close()
    
    print("################################################################")
    print("Intro")
    print("All the log entries")
    print("")
    print(log)
    print("")
    print("########")

# 1.Ips on the logs
    print("################################################################")
    print("Question 1")
    print("Some ips from gi ven")
    print("")
    get_ip(log)
    print("")
    print("########")
      

# 2.Top Ips requesting 
    print("################################################################")
    print("Question 2")    
    print("Top entries")
    print("")
    get_top10_top5url(log,log)
    print("")
    print("########")

# 2.Top Ips requesting 
    print("################################################################")
    print("Question 3")    
    print("resquest rate")
    print("")
    get_request_per_minute(log)
    print("")
    print("########")

# 6.Who is the owner of each of these IPs.
    print("########")
    print("Question 4")    
    get_owner_ip(log)
    print("########")
    print("Question 3")


# 6.Who is the owner of each of these IPs.
    print("########")
    print("Question 6")    
    get_owner_ip(log)
    print("########")
    print("Question 3")


if __name__ == "__main__":
    main()
 