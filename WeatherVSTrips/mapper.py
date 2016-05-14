#!/usr/bin/python

import datetime
import sys

key = 3
value = ""
ddate = None
ttime = None
temp = None
for line in sys.stdin:
    if("UNKNOWN" in line or len(line)<=1 ):
        continue
    datamap = line.strip().split(",")
    if datamap[0]=="Time":
        continue
    if(len(datamap)>5):#taxi data file
       temp = datamap[1].strip().split(" ")
       ddate = temp[0].replace("-","")
       ttime = temp[1].split(":")[0]
       key = "2"
       value = ddate+ttime
    else:
        if(len(datamap)>1):#weather data
            key = "1"
            value = line.strip()
    if(key != None):
        print key+","+value