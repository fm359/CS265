#!/usr/bin/env python2
#
# args.py - reading command-line args
#
# Kurt Schmidt
# 5/06
#
# Python 2.7
# on Linux 4.4.0-36-generic x86_64
# 
#	Demonstrates: sys.argv
#

import sys

argc = len( sys.argv )

print "There are", argc, "arguments"

for i in range( argc ) :
	print i, sys.argv[i]

print ""

print "--OR--"

for a in sys.argv :
	print a

