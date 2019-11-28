#!/usr/bin/env  python2

import sys

argc = len( sys.argv )

if argc > 2 :
    print "Enter 1 input file"
    exit()

inp_file = file(sys.argv[1])
print "Name\tAverage\n"
line = inp_file.readline()
while line :
        line = line.strip()
        words = line.split()
        name = words[0]
        scores = map(int, (words[1:]))
        average = sum(scores)/float(len(scores))
        print name,"\t",average
        line = inp_file.readline()
inp_file.close()
