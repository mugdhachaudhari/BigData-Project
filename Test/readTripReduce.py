#!/usr/bin/python

import sys

# inputfile = str(sys.argv[1])
# outputfile = str(sys.argv[2])
# 
# 
# fl = open(inputfile,'r')
# output = open(outputfile,'a')
 
current_key = 0
meta = []
polyData = []

def chkInside(x, y, polyData):
    n = len(polyData)
    inside =False
    x = float(x)
    y = float(y)
#     print polyData[0]
    p1x,p1y = polyData[0].split(",")
    p1x = float(p1x)
    p1y = float(p1y)
    
    for i in range(n+1):
        p2x,p2y = polyData[i % n].split(",")
        p2x = float(p2x)
        p2y = float(p2y)
#         print "x: %f, y: %f, p1x: %f, p1y: %f, p2x: %f, p2y: %f" % (x, y, p1x, p1y, p2x, p2y)
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
#                         print 'main'
                        inside = not inside
                        
#                         print inside

                        
        p1x,p1y = p2x,p2y

    return inside

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
# for line in fl:
    key, value = line.strip().split("\t", 1)
    if key == '0':
        l = value.strip().split("|")
#         print l
        zip = l[0]
        po_nm = l[1]
        borough = l[2]
        poly = []
        for i in l[5::1]:
            poly.append(i)
        polyData.append(poly)
        meta.append([zip, po_nm, borough])
        
        
    else:
        l = value.strip().split(",")
#         print key
        p_long = float(l[10])
        p_lat = float(l[11])
        d_long = l[12]
        d_lat = l[13]
         
        ind = 0
        for i in range(0, len(polyData)):
            x = chkInside(p_long, p_lat,  polyData[i])
#             print x
            if x != False:
                ind = i
                break
         
        
        p_zip = meta[ind][0]
        p_borough = meta[ind][2]
         
        ind = 0
        for i in range(0, len(polyData)):
            x = chkInside(d_long, d_lat,  polyData[i])
            if x != False:
                ind = i
                break

        d_zip = meta[ind][0]
        d_borough = meta[ind][2]
 
        l.append(p_zip)
        l.append(p_borough)
        l.append(d_zip)
        l.append(d_borough)
        val = ','.join(l)
        print "%s" % (val)
#         output.write("%s\n" %( val ))
        
