from time import time
import requests
from lxml import etree as et

from underground.tubestructure import tube

class LineStatus(object):
	def __init__(self, line):
		self.line = line
		self._line_code = line.line_code
	def currentStatus(self):
		#http://cloud.tfl.gov.uk/TrackerNet/LineStatus
		print "get status of %s" % self._line_code

class Status(object):
	def __init__(self):
		self.update_url = "http://cloud.tfl.gov.uk/TrackerNet/LineStatus"
		self.lines = {}
		self.last_update = 0
		self.update_time = 30 #TfL asks for 30 seconds between requests
		self.r = None
		for line_code, line in tube.lines.iteritems():
			self.lines[line_code] = LineStatus(line)

	def updateStatus(self):
		if (time() - self.last_update) > 30:
			self.r = requests.get(self.update_url)
			self.last_update = time()

		parser = et.XMLParser()
		tree = et.XML(self.r.content, parser)
		root = tree.getroottree()

	def getStatus(self, line_code):
		self.updateStatus()

status = Status()
