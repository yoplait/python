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

mindigits, minpalins = 2, 3
print("Count Base64 Hexa   Decimal  Octal    Binary")

from itertools import count

oct_to_64={"%02o"%i:"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@_"[i] for i in range(64)}

def base64(i):
    octalstring="{0:o}".format(i)
    if len(octalstring) % 2:
        octalstring = "0" + octalstring
    return "".join(oct_to_64[octalstring[i:i+2]] for i in range(0,len(octalstring), 2))

encoders=[base64, "{0:x}".format, str, "{0:o}".format, "{0:b}".format]

for i in count(8**(mindigits-1)):
    encodeds = [encoder(i) for encoder in encoders]
    palindromes = [encoded for encoded in encodeds if encoded[::-1]==encoded and len(encoded)>=mindigits]
    num_palins = len(palindromes)
    if num_palins >= minpalins:
        print("%-5s %-6s %-6s %-8s %-8s %s" % tuple([num_palins] + encodeds))
