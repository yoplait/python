#!/usr/bin/python

#
# Juan Carlos Perez
# perepardojc@gmail.com
# @perezpardojc
#
# Program: 
# 
# Get help python palindromic.py -h
# 
#

#imports
import os   
import sys
import re
import datetime
import time
import argparse

# functions
#def palindrome(num):
#   return num == num[::-1]
#   print "es palindromo"

def palindrome(num):
	if (num[::-1] == num):
		print "es palindromo"
		return True
	else:
		return False
# main

# this is the help in case executed -h
parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('integers', metavar='N', type=int, nargs='+', 
	help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',const=sum, default=max, 
	help='sum the integers (default: find the max)')

args = parser.parse_args()

print args.accumulate(args.integers)

#print "Hola , el numero es :", args.integers[0]
num = int(args.integers[0])

print "Hola , el numero es :",num

print id(num)

#palindrome(num)

def ReverseNumber(n, partial=0):
    if n == 0:
        return partial
    return ReverseNumber(n / 10, partial * 10 + n % 10)

trial = 123454321    

if ReverseNumber(trial) == trial:
    print "It's a Palindrome!"