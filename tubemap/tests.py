import unittest

from connections import TubeMap, TubeStation, TubeLine, build_map

class TubeMapTest(unittest.TestCase):
	def setUp(self):
		self.tubemap = build_map()
	
	def assertIsInstance(self, obj, cls):
		"""Same as self.assertTrue(isinstance(obj, cls)), with a nicer
		   default message."""
		if not isinstance(obj, cls):
			standardMsg = '%r is not an instance of %r' % (obj, cls)
			self.fail(standardMsg)

	def testDoesBuildMapReturnTubeMap(self):
		self.assertIsInstance(self.tubemap, TubeMap)

	def testOldStreetExists(self):
		self.assertEqual(self.tubemap.stations['OLD'].station_name, "Old Street")

	def testOldStreetHasOneLineAndIsNorthern(self):
		self.assertTrue(len(self.tubemap.stations['OLD'].lines) == 1)
		self.assertTrue(self.tubemap.stations['OLD'].lines.has_key("N"))
		self.assertIsInstance(self.tubemap.stations['OLD'], TubeStation)
		self.assertEqual(self.tubemap.stations['OLD'].station_name, 'Old Street')
		self.assertEqual(self.tubemap.stations['OLD'].lines['N'].line_name, "Northern")

	def testBankIsHellOnEarth(self):
		self.assertTrue(len(self.tubemap.stations['BNK'].lines) == 3)
		self.assertTrue(len(self.tubemap.stations['MON'].lines) == 2)
		self.assertIsInstance(self.tubemap.stations['BNK'].lines['C'], TubeLine)

	def testVictoriaLineHasVictoria(self):
		self.assertTrue(self.tubemap.lines['V'].stations['VIC'].station_name == "Victoria")		


if __name__ == '__main__':
	unittest.main()