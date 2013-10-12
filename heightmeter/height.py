#!/usr/bin/env python

# TO DO
# parse distance markers DONE
# objectify the parser so it can be accesed by dot notation
# use SignalSmooth to smooth the data
# calculate the total height difference DONE
# calculate the highest and the lowest point of the trip DONE
# categorize climbs (e.g. 4.5km of 5.6% climb at 24.7km)

import sys, re, pprint
import svgparser as sp
import smooth
from numpy import *
from pylab import *


svg_file = sys.argv[1]


from xml.dom import minidom

doc = minidom.parse(svg_file)  # parseString also exists
path_strings = [path for path in doc.getElementsByTagName('g')]
doc.unlink()

for x in path[0]:
  print x

pprint.pprint(path_strings)




# # call the svg parser
# raw_elev, raw_dist, raw_p = sp.svgParser(svg_file)


# # min and max values for elevation/distance and their pixel values
# min_elev = raw_elev[0]['elevation']
# max_elev = raw_elev[-1]['elevation']
# min_elev_px = raw_elev[-1]['y1']
# max_elev_px = raw_elev[0]['y1']

# min_dist = raw_dist[0]['distance']
# max_dist = raw_dist[-1]['distance']
# min_dist_px = raw_dist[0]['x1']
# max_dist_px = raw_dist[-1]['x1']

# emppx = (max_elev - min_elev) / (max_elev_px - min_elev_px)
# dmppx = (max_dist - min_dist) / (max_dist_px - min_elev_px) * 1000

# # pprint.pprint(raw_elev)

# # print 'Elevation ppx \t%3.3f m/px' % emppx
# # print 'Distance ppx \t%3.3f m/px' % dmppx
# # print 'Total distance \t%3.1f km' % max_dist
# # print 'Highest point \t%3.1f m' % max_elev
# # print 'Lowest point \t%3.1f m' % min_elev
# # print 'Difference \t%3.1f m' % (max_elev - min_elev)

# # elev_per_point = smooth.smooth(array([ round(emppx*(p['y1']-p['y2']),1) for p in raw_p ]),31)
# elev_per_point = [ round(emppx*(p['y1']-p['y2']),1) for p in raw_p ]

# elev_up = [ p for p in elev_per_point if p > 0 ]
# elev_down = [ p for p in elev_per_point if p < 0 ]

# print round(sum(elev_up),1), round(sum(elev_down),1)

# x_values = [ round(dmppx*(p['x2']+p['x1'])/2,1) for p in raw_p ]
# y_values = [ round(emppx*(p['y2']+p['y1'])/2,1) for p in raw_p ]

# # pprint.pprint(x_values[-1])
# # pprint.pprint(y_values)
# # pprint.pprint(raw_p[-1])

# # plot(elev_per_point)
# # plot(smooth.smooth(array(y_values,x_values),20))
# # show()

# # print smooth.smooth(numpy.array(y_values),20)




