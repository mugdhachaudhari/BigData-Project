#!/usr/bin/python

import sys

uniqueDriverCount_count = 1
old_key = None
old_license = None
old_month = None
count = {};
for line in sys.stdin:
    key = line.strip()
    month,license = line.split(",")
    if(old_key and old_key!=key):
        if(old_month !=month):
            count[old_month] = uniqueDriverCount_count
            uniqueDriverCount_count = 1
        else:
            uniqueDriverCount_count = uniqueDriverCount_count+1
    old_key = key
    old_license = license
    old_month = month

if (old_key != None):
        count[old_month] = uniqueDriverCount_count

for k in count.keys():
    print k+","+str(count[k])