import unittest
from status import Status, LineStatus

class TubeMapTest(unittest.TestCase):
	def setUp(self):
		self.status = Status()
	
	def assertIsInstance(self, obj, cls):
		"""Same as self.assertTrue(isinstance(obj, cls)), with a nicer
		   default message."""
		if not isinstance(obj, cls):
			standardMsg = '%r is not an instance of %r' % (obj, cls)
			self.fail(standardMsg)

	def testStatusIsActuallyStatus(self):
		self.assertIsInstance(self.status, Status)

	def testLinesIsADictAndContainsLineStatus(self):
		self.assertIsInstance(self.status.lines, dict)
		self.assertIsInstance(self.status.lines.items()[0][1], LineStatus)
		self.assertNotEqual(len(self.status.lines), 0)

if __name__ == '__main__':
	unittest.main()