#!/usr/bin/env python
#
# list_comprehensions.py - example of list comprehensions
#
# Kurt Schmidt
# 10/15
#
# Python 2.7
# on Linux 4.4.0-36-generic x86_64
# 
#	Demonstrates: comprehensions
#

	# rather than using a for loop, we can more efficiently build certain
	# lists.  Note, this serves as a map, and filter

def evalDisplay( s ) :

	r = eval( s )

	print s + ' :'
	print ' -> ' + str( r )

	return r


exps = []

exps.append( "[ i**2 for i in range(1, 17) ]" )
exps.append( "[ (i,2**i) for i in range(9) ]" )
	# to print a list
exps.append( "[ str(i) for i in [ 13, 'Heather', 2.71828] ]" )
	# we can use a conditional to make a filter
exps.append( "[ i for i in range(30) if i%2==0 ]" )
	# we have outer joins
exps.append( "[ (x,y) for x in ['a','b','c'] for y in ['1','2','3']]" )
	# we have inner joins
exps.append( "zip( ['a','b','c'], [1,2,3] )" )

for e in exps :
	evalDisplay( e )
	print ''
