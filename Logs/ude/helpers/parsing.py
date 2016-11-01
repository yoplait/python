import argparse
import sys


################################################################################################################################################
################################################################################################################################################

def function2():
	print "Esto es comando 2"
	#return()

def function1():
	print "Esto es comando 1"
	#return()


def main():
	parser = argparse.ArgumentParser(description='Work with apache logs.')

	parser.add_argument("--cmd1", help="Execute Command")
	parser.add_argument("--cmd2", help="Execute Command")
	parser.add_argument("--verbosity", help="increase output verbosity")
	
	args = parser.parse_args()
	if args.verbosity:
		print "verbosity turned on"
	if args.cmd1:
		function1()
	if args.cmd2:
		function2()


if __name__ == "__main__":
    main()

