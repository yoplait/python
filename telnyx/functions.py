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

def mifunc1(num1):
	num1=num1+1
	print "Hola , el numero mas uno es :",num1
	return False

def mifunc2(num2):
	num2=num2+2
	print "Hola , el numero mas dos es :",num2
	return False

data = int(input("Enter a number: "))
data, type(data)

print "Hola , el numero original es :",data

mifunc1(data)
mifunc2(data)