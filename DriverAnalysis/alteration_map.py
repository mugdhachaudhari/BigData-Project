#!/usr/bin/python

import sys

for line in sys.stdin:
    if("medallion" in line):
        continue
    try:
        data = line.strip().split(",")
        if(len(data)<3):
            continue
        lc = data[1]
        datetime = data[3]
        date = datetime.split("-")
        month = date[1]
    except:
        continue
    print month+","+lc