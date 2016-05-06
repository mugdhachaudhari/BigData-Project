#!/usr/bin/python

import sys
weekend_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
weekday_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
holiday_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for line in sys.stdin:
    line.strip()
    datamapped = line.split(",")
    if len(datamapped)<2:
        continue
    if datamapped[0] is "W":
        weekday_count[int(datamapped[1])] = weekday_count[int(datamapped[1])] + 1
    if datamapped[0] is "E":
        weekend_count[int(datamapped[1])] = weekend_count[int(datamapped[1])] + 1
    if datamapped[0] is "H":
        holiday_count[int(datamapped[1])] = holiday_count[int(datamapped[1])] + 1

print "Hour,Weekday,Weekend,Holiday"
for i in range(0,24):
    count = i
    print str(i)+","+str(weekday_count[i])+","+str(weekend_count[i])+","+str(holiday_count[i])