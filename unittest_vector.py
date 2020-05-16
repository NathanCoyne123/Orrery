import unittest
from vector import Vector

class VectorTestCase(unittest.TestCase):
    def assertAlmostEqual(self, a, b):
        unittest.TestCase.assertAlmostEqual(self, a.x, b.x)
        unittest.TestCase.assertAlmostEqual(self, a.y, b.y)
        unittest.TestCase.assertAlmostEqual(self, a.z, b.z)
