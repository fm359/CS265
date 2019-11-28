#!/usr/bin/env python
#
# input.py - example of reading the standard input.
#
# Kurt Schmidt
# 2/12
#
# Python 2.7
# on Linux 4.4.0-36-generic x86_64
# 
#	Demonstrates: try raise except finally
#


# all exceptions *should* inherit, directory or indirectly, from Exception

class MyError( Exception ) :
	def __init__( self, value ):
		self.value = value
	def __str__( self ):
		return repr( self.value )

class UnknownError( Exception ) :
	def __init__( self, value ):
		self.value = value
	def __str__( self ):
		return repr( self.value )


def foo() :
	'''throws MyError, for fun'''

	i = 'something useless'
	raise MyError( 'foo threw me' )

	return 'never get this string'

def bar() :
	'''throws UnknowError, for fun'''

	i = 'something useless'
	raise MyError( 'bar threw me' )

	return 'never get this string'


try :   # in a try block is code that might throw an exception
	print "This line will happen (if print worked)"
	foo()
	print "This line will never happen"
except MyError, e :
	print "Caught a MyError:", e
	print "We can rethrow (raise) the same error, or a different one, " + \
				"or allow processing to continue"
except Exception, e :   # will catch anything inherited from Exception
	print "Caught a generic Exception", e
except :  # This will catch anything as yet uncaught
	print "Caught something, I dunno what"
	print "Don't know what to do, so, rethrowing:"
	raise
else :
	print "This line will only happen if NO exception is thrown"
finally :
	print "This line *always* happens"

print "This line will *only* happen if the exception was caught, " + \
			"and not rethrown, or, no exception was thrown."

