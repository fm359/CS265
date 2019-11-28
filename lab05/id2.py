#!/usr/bin/env  python2

import sys

argc = len( sys.argv )

if argc > 2 :
    print "Enter 1 input file"
    exit()
elif argc == 2 :
    inp_file = file(sys.argv[1])
    lines = inp_file.readlines()
    inp_file.close()
elif argc == 1 :
    lines = sys.stdin.readlines()
    print "\n"

print "ID\tName\n"
ids_dict = {}
for line in lines :
    line.strip()
    words = line.split()
    ID = int(words[0])
    name = (' ').join(words[1:])
    ids_dict[ID] = name

for key in sorted(ids_dict):
    print "%s\t%s" % (key, ids_dict[key])
