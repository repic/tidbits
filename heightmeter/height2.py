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
from numpy import array 
import pylab as plt


svg_file = sys.argv[1]


# call the svg parser
raw_elev, raw_dist, raw_p = sp.svgParser(svg_file)


# min and max values for elevation/distance and their pixel values
min_elev = raw_elev[0]['elevation']
max_elev = raw_elev[-1]['elevation']
min_elev_px = raw_elev[-1]['y1']
max_elev_px = raw_elev[0]['y1']

min_dist = raw_dist[0]['distance']
max_dist = raw_dist[-1]['distance']
min_dist_px = raw_dist[0]['x1']
max_dist_px = raw_dist[-1]['x1']

emppx = (max_elev - min_elev) / (max_elev_px - min_elev_px)
dmppx = (max_dist - min_dist) / (max_dist_px - min_elev_px) * 1000

print 'Elevation ppx \t%3.3f m/px' % emppx
print 'Distance ppx \t%3.3f m/px' % dmppx
print 'Total distance \t%3.1f km' % max_dist
print 'Highest point \t%3.1f m' % max_elev
print 'Lowest point \t%3.1f m' % min_elev
print 'Difference \t%3.1f m' % (max_elev - min_elev)

x_values = [ round(dmppx*(p['x2']+p['x1'])/2,1) / 1000 for p in raw_p ]
y_values = [ round(max_elev - emppx*(p['y2']+p['y1'])/2,1) + min_elev for p in raw_p ]
y_smooth = list(smooth.smooth(array(y_values), 40, 'bartlett'))

elev_per_point = [ round(y_smooth[i+1]-y_smooth[i],1) for i in range(len(y_smooth)-1) ]
elev_up = [ p for p in elev_per_point if p > 0 ]
elev_down = [ p for p in elev_per_point if p < 0 ]

# pprint.pprint(elev_per_point)


print round(sum(elev_up),1), round(sum(elev_down),1)
plt.plot(x_values, y_values, linewidth=8, linestyle='-', color='g', label='Square')
plt.plot(x_values, y_smooth, linewidth=3, linestyle='-', color='r', label='Square')

plt.show()

