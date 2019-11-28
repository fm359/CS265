#!/usr/bin/env python
#
# optparse.py - parsing command-line arguments using optparse
#		Allows for long options, provides its own help
#
# Kurt Schmidt
# 5/14
#
# Python 2.7
# on Linux 4.4.0-36-generic x86_64
# 
#	Demonstrates: optparse
#

import sys
from optparse import OptionParser

usage = "usage: %prog [options]"
op = OptionParser( usage=usage )

	# note, the default action is simply "store"
op.add_option( '-c', '--chocolate', action='store_true', dest='bChoc', 
								default='True', help='Signals desire for chocolate' )
op.add_option( '-C', '--num_chars', type='int', dest='lenPref',
								default=0, help='Number of characters' )
op.add_option( '-k', '--knot', type='choice',
								choices=('klemheist', 'zeppelin bend', 'bowline'),
								help='Specify type of knot' )
op.add_option( '-y', help='Flag w/no long option', type='string' )
op.add_option( '-z', help='Flag w/no long option' )

(opts, args) = op.parse_args()

print 'Here are the options:', opts
print 'Here are the arguments:', args

