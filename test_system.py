import unittest_vector
import unittest

from vector import Vector
from celestial_body import CelestialBody
from system import System

class TestSystem(unittest.TestCase):
    def setUp(self):
        self.zero = Vector(0,0,0)
        
    def test_ShouldNeverMoveSingleStationaryBody(self):
        body = CelestialBody("N",1e25,Vector(4,7,9),self.zero,self.zero)
        system = System("Single Body", [body])
        system.update(10000)
        self.assertTrue(body.position == Vector(4,7,9))

    def test_ShouldMoveAtConstantVelocitySingleMovingBody(self):
        body = CelestialBody("N",1e25,self.zero,Vector(10,15,50),self.zero)
        system = System("Single Body", [body])
        system.update(10)
        self.assertTrue(body.velocity == Vector(10,15,50))
        self.assertTrue(body.position == Vector(100,150,500))

    def test_ShouldMoveTwoStationaryBodiesDirectlyTowardsEachOther(self):
        body1 = CelestialBody("N",1e25,Vector(-100,0,0),self.zero,self.zero)
        body2 = CelestialBody("M",1e25,Vector(100,0,0),self.zero,self.zero)
        system = System("Dual Body", [body1,body2])
        system.update(10)
        self.assertTrue(body1.velocity == Vector.mult(-1,body2.velocity))
        self.assertTrue(body1.velocity != body2.velocity)
        self.assertTrue(Vector.add(body1.velocity,body2.velocity) == self.zero)
        # Do position test
        
if __name__ == '__main__':
    unittest.main()
