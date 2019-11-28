#!/usr/bin/env python2
#
# gen_func.py - another way of faking a static variable, using a
#		generator function.  Essentially, delayed evaluation of a sequence
#
# Kurt Schmidt
# 12/07
#
# Python 2.7
# on Linux 4.4.0-36-generic x86_64
# 
# DEMONSTRATES:  yield
#

def get_next_filename_gen( startIdx=0 ) :
	'''Returns a iterator of filenames'''
	idx = startIdx
	while True :	# Note, this stream is infinite
		s = str( idx )
		s = s.rjust( 5, '0' )
		yield 'tmp' + s
		idx += 1

def main() :
	"""A "main" function, called below.
	   This is a doc string, serves as a nice function header description"""
	
		# get your iterator 
	filename = get_next_filename_gen( 8 )

		# Use your iterator
	print "here's a filename:", filename.next()
	print "and the next:", next( filename )
	print "and the next:", next( filename )
	print "and the next:", next( filename, None ) # will never be used here

if __name__ == "__main__" :
	main()
