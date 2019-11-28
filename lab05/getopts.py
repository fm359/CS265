#!/usr/bin/env python2
#
# getopts.py - parsing command-line arguments
#
# Kurt Schmidt
# 2/07
#
# Python 2.7
# on Linux 4.4.0-36-generic x86_64
# 
#	Demonstrates: getopts
#

import sys
from getopt import getopt

scriptname = sys.argv.pop( 0 ) # shift off the scriptname
optlist, args = getopt( sys.argv, "qf:v" )

print "Here are your options (and their args), as a list of tuples:\n\t" + str( optlist )
print "\nHere are the non-option args:\n\t" + str( args )

