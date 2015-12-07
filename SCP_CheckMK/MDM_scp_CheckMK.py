#!/usr/bin/python
#
#
#
import os
import platform
import argparse

# this is the help in case executed -h
parser = argparse.ArgumentParser(description='Connect MDM CheckMK boxes and get the file.')

parser.add_argument('integers', metavar='N', type=int, nargs='+', 
	help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',const=sum, default=max, 
	help='sum the integers (default: find the max)')

args = parser.parse_args()


print "Your systems is :"
print os.name
print platform.system()
print platform.release()

print args.accumulate(args.integers)

