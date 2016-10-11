#!/usr/bin/python

#
# Juan Carlos Perez
# perepardojc@gmail.com
# @perezpardojc
#
# Program: 
# 
# Program to convert in any bases
# How to use: execute  # python converter.py
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


def My_Bases(argument):
    switcher = {
        2: "Binary - Base 2",
        3: "Base 3",
        4: "Base 4",
        5: "Base 5",
        6: "Base 6",
        7: "Base 7",
        8: "Octal - Base 8",
        9: "Base 9",
        10: "Decimal - Base 10",
        11: "Base 11",
        12: "Base 12",
        13: "Base 13",
        14: "Base 14",
        15: "Base 15",
        16: "Hexadecimal - Base 16",
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
#
# main area
#

print("Comienzo of my super palindrome")

for base in itertools.count(start=2, step=1): #base
    for num in itertools.count(start=0, step=1): #numbers
        print("Numero en decimal:                              ",num)
        print("Base en:                                  ",My_Bases(base),base10toN(num,base))
        print(Palindrome_Number(int(base10toN(num,base))))
        #print("Numero en base binaria:      ",base10toN(num,base))
        time.sleep (50.0 / 1000.0);
        if (num==10):
            break
    if (base==16):
        break

print("")
print("Final")


