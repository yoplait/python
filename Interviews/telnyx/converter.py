#!/usr/bin/python

#
# Juan Carlos Perez
# perepardojc@gmail.com
# @perezpardojc
#
# Program: 
# 
# Program to convert in any bases
#  
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

def My_Bases(argument):
    switcher = {
        2: "Binary",
        3: "Three",
        4: "Fourth",
    }
    return switcher.get(argument, "nothing")

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

print("Comienzo of my super palindrome")

for base in itertools.count(start=2, step=1):
    for num in itertools.count(start=0, step=1):
        print("Numero en decimal:   ",num)
        print("Base en:  ",My_Bases(base),base10toN(num,base))
        #print("Numero en base binaria:      ",base10toN(num,base))
        time.sleep (50.0 / 1000.0);
        if (num==32):
            break
    if (base==16):
        break

print("")
print("Final")


