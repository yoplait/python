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
            # print(dict_ips[aws_ip])
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
    


def main():

	"""Runs program and handles command line options"""
	p = optparse.OptionParser(description='Prints out the request count per minute.')

	p.add_option('-r','--requestrate',  default="")

	options, arguments = p.parse_args()

	if options.requestrate:
		udemy3(options.requestrate)


if __name__ == '__main__':
	main()