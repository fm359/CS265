#!/usr/bin/env python2
#
# func_obj.py - A callable object.  Very much like a c++ function object
#
# Kurt Schmidt
# 12/07
#
# Python 2.7
# on Linux 4.4.0-36-generic x86_64
# 
# DEMONSTRATES:  __call__
#

class get_next_filename_gen :
	'''a function object, can be called much like a function'''

	def __init__( self, startIdx=0 ) :
		self.idx = startIdx

	def __call__( self ) :
		'''Returns a serial of filenames'''
		s = str( self.idx )
		self.idx += 1
		s = s.rjust( 5, '0' )
		return 'tmp' + s

def main() :
	"""A "main" function, called below.
	   This is a doc string, serves as a nice function header description"""
	
	fnameObj = get_next_filename_gen( 8 )

	print "here's a fnameObj:", fnameObj()
	print "and the next:", fnameObj()
	print "and the next:", fnameObj()
	print "and the next:", fnameObj()

if __name__ == "__main__" :
	main()
