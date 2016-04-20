#!/usr/bin/python

import sys
import operator




# input comes from STDIN (stream data that goes to the program)
# inputfile = str(sys.argv[1])
# # outputfile = str(sys.argv[2])
# fl = open(inputfile,'r')
# for line in fl:
for line in sys.stdin:

    keys, values = line.strip().split("\t", 1)
    print "%s" %(values)
