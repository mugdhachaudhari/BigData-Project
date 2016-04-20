#!/usr/bin/env python
import sys
sys.path.append('.')
import matplotlib
matplotlib.use('Agg')
from matplotlib.path import Path
from rtree import index as rtree
import numpy, shapefile, time
import random
import os
from datetime import datetime
from datetime import date


def findNeighborhood(location, index, neighborhoods, recursionTimes):
    '''Find the location's neighborhood according to its latitude and longitude. And if we cannot find its neighborhood, we will find its nearest neighborhood by changing its latitude and longitude by 0.1. The recursion times are 4 times at most. If we cannot find its neighborhood, the function will return -1.'''

    if recursionTimes > 0:
        return -1
    match = index.intersection((location[0], location[1], location[0], location[1]))
    for a in match:
        if any(map(lambda x: x.contains_point(location), neighborhoods[a][1])):
            return a

    # Use a random number to choose a direction to do recursion
    n = random.randint(1, 4)

    if n == 1:
        longitude = location[0] + 0.1
        latitude = location[1]
        newLocation = (longitude, latitude)
        X = findNeighborhood(newLocation, index, neighborhoods, recursionTimes + 1)
        return X
    elif n == 2:
        longitude = location[0] - 0.1
        latitude = location[1]
        newLocation = (longitude, latitude)
        X = findNeighborhood(newLocation, index, neighborhoods, recursionTimes + 1)
        return X
    elif n == 3:
        longitude = location[0]
        latitude = location[1] + 0.1
        newLocation = (longitude, latitude)
        location[1] += 0.1
        X = findNeighborhood(newLocation, index, neighborhoods, recursionTimes + 1)
        return X
    elif n == 4:
        longitude = location[0]
        latitude = location[1] - 0.1
        newLocation = (longitude, latitude)
        X = findNeighborhood(newLocation, index, neighborhoods, recursionTimes + 1)
        return X

    return -1


def readNeighborhood(shapeFilename, index, neighborhoods):
    sf = shapefile.Reader(shapeFilename)
    for sr in sf.shapeRecords():
        if sr.record[1] not in ['New York', 'Kings', 'Queens', 'Bronx']: continue
        # print sr.record
        # print sr.shape.parts[1:]
        paths = map(Path, numpy.split(sr.shape.points, sr.shape.parts[1:]))
        # print paths
        bbox = paths[0].get_extents()
        # print bbox
        map(bbox.update_from_path, paths[1:])
        index.insert(len(neighborhoods), list(bbox.get_points()[0])+list(bbox.get_points()[1]))
        # print list(bbox.get_points()[0])+list(bbox.get_points()[1])
        neighborhoods.append((sr.record[3], paths, sr.record[2]))

    neighborhoods.append(('UNKNOWN', None, 'UNKNOWN'))


def mapper():
    index = rtree.Index()
    neighborhoods = []
    # readNeighborhood('nynta.shp', index, neighborhoods)
    readNeighborhood('ZillowNeighborhoods-NY.shp', index, neighborhoods)
    agg = {}

    # inputfileP = str(sys.argv[1])
    # flp = open(inputfileP,'r')
    # filename = inputfileP
    # for line in flp:

    for line in sys.stdin:
        try:
            filename = os.environ['mapreduce_map_input_file']
        except KeyError:
            filename = os.environ['map_input_file']


        line = line.strip('\n')
        values = line.split(',')


        if 'VendorID' in line or 'vendor_id' in line :
            continue

        if 'yellow' in filename:
            try:
                pickup_location = (float(values[5]), float(values[6]))
                dropoff_location = (float(values[9])), float(values[10])
                pickupDate = values[1][:10]

            except Exception:
                pass

        else:
            try:
                pickup_location = (float(values[5]), float(values[6]))
                dropoff_location = (float(values[7])), float(values[8])
                pickupDate = values[1][:10]

            except Exception:
                pass


        try:
            pickup_neighborhood = findNeighborhood(pickup_location, index, neighborhoods, 0)
            dropoff_neighborhood = findNeighborhood(dropoff_location, index, neighborhoods, 0)

            pickupRegion = neighborhoods[pickup_neighborhood][0]
            pickupMain = neighborhoods[pickup_neighborhood][2]

            dropoffRegion = neighborhoods[dropoff_neighborhood][0]
            dropoffMain = neighborhoods[dropoff_neighborhood][2]

            val = [line, pickupRegion, pickupMain, dropoffRegion, dropoffMain]
            valj = ','.join(val)
            print "%s\t%s" % (pickupDate, valj)
            # print line + "," + pickupRegion + ","  + dropoffRegion


        except Exception:
            pass

    # fl.close()
if __name__ == '__main__':
    mapper()
