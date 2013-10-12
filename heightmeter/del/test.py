#!/usr/bin/env python

dl = [ {'ele':'12', 'hei':'13'}, {'ele':'14', 'hei':'15'}, {'ele':'16', 'hei':'17'} ]

print dl


for point in dl:
	for key in point:
		try:
			point[key]=float(point[key])
		except:
			pass	

print dl



