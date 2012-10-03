from underground.tubestructure import tube
class Status(object):
	def currentStatus(self):
		#http://cloud.tfl.gov.uk/TrackerNet/LineStatus
		print "status"

	def __init__(self):
		self.lines = tube.lines


status = Status()
