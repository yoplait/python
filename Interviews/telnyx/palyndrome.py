#!/usr/bin/python

#
# Juan Carlos Perez
# perepardojc@gmail.com
# @perezpardojc
#
# Program: 
# 
# # Program to check if a string
#  is palindrome or not
# 
#

#imports
import os   
import sys
import re
import datetime
import time
import argparse
import itertools


print('!* To Find Palindrome Number')

def palinum(n):
    results = list()
    for each in range(n):
        s = str(each)
        if s == ''.join(reversed(s)):
            results.append(each)
    return results


def Palindrome_Number(n):
    #n = input('Enter Number to check for palindromee:   ')
    print "Hi , The number is  :",n
    print ""
    m=n
    a = 0
    while(m!=0):
        a = m % 10 + a * 10
        m = m / 10

    if( n == a):
        print('%d is a palindrome number' %n)
    else:
        print('%d is not a palindrome number' %n)


def base10toN(num, base):
    """Change ``num'' to given base
    Upto base 36 is supported."""

    converted_string, modstring = "", ""
    currentnum = num
    if not 1 < base < 37:
        raise ValueError("base must be between 2 and 36")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return converted_string

def Auto_Palindrome_Number():
	print("Comienzo")
	for i in itertools.count(start=0, step=1):
	    print(i)
	    Palindrome_Number(i)
	    time.sleep (50.0 / 1000.0);
	    if (i==100):
	   		break
	print("")
	print("Final")
	return false



counter=1
Auto_Palindrome_Number()
#Palindrome_Number()