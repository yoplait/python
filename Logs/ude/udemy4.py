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

    return()
    


def main():

	"""Runs program and handles command line options"""
	p = optparse.OptionParser(description='--start <HH:MM>')

	p.add_option('-s','--start',  default="")

	options, arguments = p.parse_args()
    
	if options.start:
		udemy4(options.start)


if __name__ == '__main__':
	main()