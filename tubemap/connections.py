from lines import lines
from stations import central, district, hammersmith_city, circle, jubilee
from stations import metropolitan, nothern, piccadilly, victoria, waterloo_city
from stations import line_mapper

class TubeStation(object):
	"""A station object in the TubeMap
	All lines that interconnect are available in the .lines dict
	"""
	def __init__(self, station_code, station_name):
		self.station_code = station_code
		self.station_name = station_name
		
		self.lines = {}
	def __repr__(self):
		return self.station_name

class TubeLine(object):
	"""A tube object in the TubeMap
	All stations that are on this line are available in the .stations dict
	"""
	def __init__(self, line_code, line_name):
		self.line_code = line_code
		self.line_name = line_name

		self.stations = {}
	def __repr__(self):
		return self.line_name

class TubeMap(object):
	"""The TubeMap object which holds all stations and lines
	"""
	def __init__(self):
		self.stations = {}
		self.lines = {}

def build_map():
	"""Builds a complete TubeMap object from the lines/stations files
	If there are new stations (ha!) or new lines (hahaha!, well CrossRail eventually)
	add them in the stations and lines files and they will be added to the TubeMap
	"""
	#Update in 2019 for CrossRail.. Because I don't believe the 2018 prediction

	#this could easily be sped up by doing a single loop
	#but, i'm lazy and this works.. if you want to refactor
	#go nuts but, i'm sure there's more broken things than
	#this in the entire app

	#build tube lines
	tmap = TubeMap()
	for code, name in lines.iteritems():
		tmap.lines[code] = TubeLine(code, name)

	#build tube stations
	for line_code, line in tmap.lines.iteritems():
		for station_code, station_name in line_mapper[line_code].iteritems():
			if not tmap.stations.has_key(station_code):
				tmap.stations[station_code] = TubeStation(station_code, station_name)
			tmap.lines[line_code].stations[station_code] = tmap.stations[station_code]

	'''all_stations = None
	for code, line in line_mapper.items():
		if all_stations is None:
			all_stations = line
		else:
			all_stations.update(line)
	for code, name in all_stations.iteritems():
		tmap.stations[code] = TubeStation(code, name)'''
	
	
	#build inter-connects

	#loop over all stations and find lines that have that station
	for station_code, station in tmap.stations.iteritems():
		#'OXC', TubeLine(Oxford Circus)
		for line_code, line_stations in line_mapper.iteritems():
			#'P', dict(Piccadilly)
			if line_stations.has_key(station_code):
				#station is on this line
				tmap.stations[station_code].lines[line_code] = tmap.lines[line_code]

	return tmap

if __name__ == '__main__':
	tubemap = build_map()
	print tubemap.stations

