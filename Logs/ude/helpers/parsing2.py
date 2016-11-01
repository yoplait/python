#!/usr/bin/python
# -*- coding: utf-8 -*-

import optparse
import argparse
import sys

################################################################################################################################################
################################################################################################################################################

def mifunc1():
	print "solo lo que tengo en func"

def mifunc2(opts):
	print opts

def main():
	"""Runs program and handles command line options"""

	p = optparse.OptionParser(description='Finds MAC Address of IP address(es)')
	
	p.add_option('-p','--person',  default="")
	p.add_option('-a','--cmd1',  default="")
	p.add_option('-b','--cmd2',  default="")
  	p.add_option('-v', '--verbose', action ='store_true', help='returns verbose output')

	options, arguments = p.parse_args()
   	
	print len(arguments) 

	if options.person:
		print 'Hello %s' % options.person	

	if options.cmd1:
		mifunc1()

	if options.cmd2:
		mifunc2(options.cmd2)

   	#print 'Hello %s' % options.person



if __name__ == '__main__':
	main()