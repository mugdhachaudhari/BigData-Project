#!/usr/bin/python

import sys

import holidays
from datetime import date

us_holidays = holidays.UnitedStates()

def checkDateType(year,month,day):
    if date(year, month, day) in us_holidays:
        return "H"
    d = date(year,month,day).weekday()
    if d>= 0 and d<5:
        return "W"
    else:
        return "E"

count =0
for line in sys.stdin:
    try:
        line.strip()
        count = count+1
        datamapped = line.split(",")
        if len(datamapped)<2:
            continue
        key = datamapped[19]
        if key == 'UNKNOWN':
            continue
        amount = datamapped[18]
        if(amount <=0 ):
            continue
        amount_cent = int(round(float(amount.strip('$'))*100))
        d, t = datamapped[1].split(" ")
        t.strip()
        d.strip()
        y, m, day = d.split("-")
        hr,min,sec = t.split(":")
        datetype = checkDateType(int(y),int(m),int(day))
        print datetype+","+hr+","+str(amount_cent)
    except:
        continue