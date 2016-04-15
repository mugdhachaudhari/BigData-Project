#!/usr/bin/python

import sys
import os

# input comes from STDIN (stream data that goes to the program)

# inputfileP = str(sys.argv[1])
# flp = open(inputfileP,'r')
# inputfileS = str(sys.argv[2])
# 
# outputfile = str(sys.argv[3])
# output = open(outputfile,'a')

# for line in flp:
for line in sys.stdin:

    try:
        filename = os.environ['mapreduce_map_input_file']
    except KeyError:
        filename = os.environ['map_input_file']

#     filename = 'trips'
    if 'trip' in filename:
        if line.strip() == 'medallion,hack_license,vendor_id,rate_code,store_and_fwd_flag,pickup_datetime,dropoff_datetime,passenger_count,trip_time_in_secs,trip_distance,pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude':
            continue
        value = line.strip()    
        key = 1
        print ("%s\t%s" %( key, value ))
#         output.write("%s\t%s\n" %( key, value ))
    else:
        if 'properties/OBJECTID' in line.strip():
            continue

        l = line.strip().split(",")
        zip = l[2]
        po_nm = l[3]
        borough = l[5]
        lng = l[10]
        lat = l[11]
            
        poly = []
        cord = []
        for i in l[13::1]:
            if i:
                if (len(cord) == 2 or len(cord) == 0):
                    cord = []
                    cord.append(i)
                else:
                    cord.append(i)
                    poly.append(','.join(cord))
        polyStr = '|'.join(poly)
        #     print "%s" %(polyStr)   
        att = [zip, po_nm, borough, lng, lat, polyStr]
#             meta.append([zip, po_nm, borough, lng, lat])
#             polyData.append(poly)
        attVal = '|'.join(att)
        zKey = 0
        print ("%s\t%s" %( zKey, attVal ))
#         output.write("%s\t%s\n" %( zKey, attVal ))
        
           

