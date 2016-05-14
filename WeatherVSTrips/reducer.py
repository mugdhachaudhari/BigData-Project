#!/usr/bin/python

import datetime
import sys

rain = 0
fog = 0
snow = 0
clear = 0
cloud = 0
t_rain = 1
t_fog = 1
t_snow = 1
t_clear = 1
t_cloud = 1
value = None
stuff = {}
for line in sys.stdin:
    datamap = line.strip().split(",")
    if (datamap[0] == "1"):#weather data
        stuff[datamap[1]]= datamap[2]
    elif datamap[0]== "2": #trip data
        value = stuff[datamap[1]]
        if (len(value) != None):
            if("Clear" in value):
                clear = clear+1
            elif ("Rain" in value or value == "Mist"):
                rain = rain+1
            elif (value == "Fog" or value == "Haze"):
                fog = fog+1
            elif ("Snow" in value):
                snow = snow+1
            elif ("Cloud" in value or value == "Overcast" or "cloud" in value):
                cloud =cloud+1
            else:
                continue
for j in stuff.keys():
    if("Clear" in stuff[j]):
        t_clear = t_clear+1
    elif("Rain" in stuff[j] or stuff[j] == "Mist"):
        t_rain = t_rain + 1
    elif (stuff[j] == "Fog" or stuff[j] == "Haze"):
        t_fog = t_fog + 1
    elif ("Snow" in stuff[j]):
        t_snow = t_snow + 1
    elif ("Cloud" in stuff[j] or stuff[j] == "Overcast"):
        t_cloud = t_cloud + 1
    else:
        continue
if t_clear>1:
    t_clear = t_clear -1
if t_fog >1:
    t_fog = t_fog - 1
if t_cloud>1:
    t_cloud = t_cloud-1
if t_rain > 1:
    t_rain = t_rain - 1
if t_snow>1:
    t_snow = t_snow -1
print "Type,Count"
print "Clear,"+str(float(clear/t_clear))
print "Snow,"+str(float(snow/t_snow))
print "Rain,"+str(float(rain/t_fog))
print "Fog,"+str(float(fog/t_fog))
print "Cloud,"+str(float(cloud/t_cloud))