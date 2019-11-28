#!/usr/bin/env python
#
# calc.py - implements a calculator that parses an infix expression into postfix, and then evaluates it
#
# Farhan Muhammad
# 05/2018
#

import sys

operators = set(['+', '-', '*', '/', '%', '(', ')']) # set of operators
precedence = {'+':1, '-':1, '*':2, '/':2, '%':2}     # assign priority for each operator

# Function to convert infix expression into postfix

def infix2postfix(expr):
    expr = expr.split(' ')        		  # splitting the input string at whitespaces
    expr.append(')')              		  # makes it easier to compute multiple digit operands
    stack = ['(']
    output = ''
    for char in expr:
        if char not in operators: 		  # append to the postfix expression
            output += char
	    output += ' '
        elif char == '(':         		  # push it onto the stack
            stack.append('(')
        elif char == ')':         		  # pop operators from the stack and append to the postfix expression
            while stack and stack[-1] != '(':     # until a left parenthesis is encountered on the stack
                output += stack.pop()
	    output += ' '
            stack.pop()
        else:					  # pop operators from the stack and append to the postfix expression
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]: # logic for precedence
                output += stack.pop()
                output += ' '
            stack.append(char)
    while stack:				  # pop until the end of the expression is reached
        output += stack.pop()
	output += ' '
    return output

# Function to evaulate the postfix expression
def evalPostfix(expr):
    expr = expr.split(' ')
    if expr[-1] == '':
	expr.pop()				  # remove blank element created due to presence of newline
    stack = []
    for char in expr:
        if char not in operators: 		  # push operands to stack
            stack.append(int(char))
        else:					  # implement logic for computing operations
            y = stack.pop()			  # y <- pop top value
            x = stack.pop()			  # x <- pop top value
            out = {'+':x+y, '-':x-y, '*':x*y, '/':x/y, '%':x%y}[char] # operate
            stack.append(out)			  # push result onto stack
    return stack[-1]

# Function to generate tokens for each line of expressions from input file
def tokenise(f_in):

    for line in f_in:
        line = line.strip('\n')
        yield line

def main(args):
    if len(args) < 2:               		  # read stdin if no input file given
        f = sys.stdin
    elif len(args) > 2:             		  # only accept one input argument
	print "Too many arguments"
	sys.exit()
    else:
        f = open(args[1])
    tokens = tokenise(f)
    for t in tokens:				  # perform conversion and calculation for each line of expressions
     	a = infix2postfix(t)
 	b = evalPostfix(a)
        print a,'=',b

    return 0

if  __name__ == '__main__':
     sys.exit( main( sys.argv ))
