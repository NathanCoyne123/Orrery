import unittest_vector
import unittest

from vector import Vector
from celestial_body import CelestialBody

class TestCelestialBody(unittest_vector.VectorTestCase):
    def setUp(self):
        self.nonZero = Vector (3,4,5)
        self.nonZero2 = Vector (8,1,2)
        self.nonZero3 = Vector (7,9,3)
        self.zero = Vector (0,0,0)

    def test_ShouldNotMoveAtZeroVelocityAndAcceleration(self):
        body = CelestialBody("Sun", 1E26, self.zero, self.zero, self.zero)
        body.update( 10000)
        self.assertTrue( body.position == self.zero)

    def test_ShouldMoveInSmallTimeIntervalAtZeroAcceleration(self):
        body = CelestialBody("Sun", 1E26, self.nonZero, self.nonZero2, self.zero)
        body.update( 0.25)
        self.assertTrue( body.position == Vector(5,4.25,5.5))

    def test_ShouldMoveAtIncreasingVelocityWithConstantAcceleration(self):
        body = CelestialBody("Sun", 1E26,
                             self.nonZero, self.nonZero2, self.nonZero3)
        body.update(1)
        self.assertTrue( body.velocity == Vector(15,10,5))
                    
    def test_ShouldMoveAtIncreasingRateOfChangeOfPositionWithConstantAcceleration(self):
        body = CelestialBody("Sun", 1E26,
                             self.nonZero, self.nonZero2, self.nonZero3)
        body.update(1)
        self.assertTrue( body.position == Vector(14.5, 9.5, 8.5))

    def test_ShouldGiveSameOutputNoMatterTheTickFrequency(self):
        body = CelestialBody("Sun", 1E26,
                             self.nonZero, self.nonZero2, self.nonZero3)
        for _ in range(1,11):
            body.update(0.1)

        print(body.position)
        print(body.velocity)
            
        self.assertAlmostEqual( body.position, Vector(14.5, 9.5, 8.5))
        self.assertAlmostEqual( body.velocity, Vector(15,10,5))
        
if __name__ == '__main__':
    unittest.main()
