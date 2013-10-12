
import re

# get raw pixel and height data from the svg file
def svgParser(svgfile):
	with open(svgfile) as f:
		
		# regex for getting raw data from svg file
		regex_data_alt = re.compile(r'(?<=\=\")[\w\d\. \#]+(?=\")|(?<=\>)\d+\.*\d*(?= m)')
		regex_data_dist = re.compile(r'(?<=\=\")[\w\d\. \#]+(?=\")|(?<=\>)\d+\.*\d*(?= km)')
		regex_label = re.compile(r'(?<= )[\w\d\. \-]+(?=\=\")')
		regex_point = re.compile(r'(?<= )[\w\d\. \-]+(?=\=\")')

		# Get altitude ticks
		raw_Altitudes = [re.findall(regex_data_alt,line) for line in f if 'altitude y line' in line]
		f.seek(0)
		raw_Altitudes_labels = [re.findall(regex_label,line) for line in f if 'altitude y line' in line]
		f.seek(0)

		for line in raw_Altitudes_labels:
			line.append('elevation')
		
		altitudes = [dict(zip(raw_Altitudes_labels[x], raw_Altitudes[x])) for x in range(len(raw_Altitudes_labels))]


		# Get distance ticks
		raw_Distances = [re.findall(regex_data_dist,line) for line in f if 'distance x line' in line]
		f.seek(0)
		raw_Distances_labels = [re.findall(regex_label,line) for line in f if 'distance x line' in line]
		f.seek(0)

		for line in raw_Distances_labels:
			line.remove('transform')
			line.append('distance')
		

		distances = [dict(zip(raw_Distances_labels[x], raw_Distances[x])) for x in range(len(raw_Distances_labels))]
		

		# Get data points
		raw_Points = [re.findall(regex_data_alt,line) for line in f if 'id="t' in line ]
		f.seek(0)
		raw_Points_labels = [re.findall(regex_label,line) for line in f if 'id="t' in line]
		f.seek(0)

		points = [dict(zip(raw_Points_labels[x], raw_Points[x])) for x in range(len(raw_Points_labels))]

		# Convert string numbers to float values
		for dicts in [altitudes, distances, points] :
			for point in dicts:
				for key in point:
					try:
						point[key] = float(point[key])
					except ValueError:
						pass

		return altitudes, distances, points

