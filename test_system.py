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
        self.assertTrue(Vector.add(body1.position,body2.position) == self.zero)
        self.assertTrue(body1.position.y == body2.position.y)
        self.assertTrue(body1.position.z == body2.position.z)
        self.assertTrue(body1.position.y == 0)
        self.assertTrue(body1.position.z == 0)
        
    def test_ShouldAccelerateASmallBodyTowardsABigOne(self):
        body1 = CelestialBody("N",1e30,Vector(-100,0,0),self.zero,self.zero)
        body2 = CelestialBody("M",1e23,Vector(100,0,0),self.zero,self.zero)
        system = System("Dual Body", [body1,body2])
        system.update(10)
        self.assertTrue(body1.calcSpeed() - body2.calcSpeed() < 0)
        self.assertTrue(body1.position.x + body2.position.x < 0)
        self.assertTrue(body1.position.y == body2.position.y)
        self.assertTrue(body1.position.z == body2.position.z)
        self.assertTrue(body1.position.y == 0)
        self.assertTrue(body1.position.z == 0)

    def test_ShouldAccelerateASmallBodyWithSmallStartingVelocityTowardsABigOne(self):
        body1 = CelestialBody("N",6e24,Vector(0,0,0),self.zero,self.zero)
        body2 = CelestialBody("M",1e3,Vector(1e7,0,0),Vector(0,1000,0),self.zero)
        system = System("Dual Body", [body1,body2])
        distance = 1e7
        for _ in range(1,101):
            system.update(1)
            new_distance = CelestialBody.calcDistance(body1,body2)
            self.assertTrue(new_distance < distance)
            distance = new_distance

    def test_ShouldNotAccelerateASmallBodyWithLargeStartingVelocityTowardsABigOne(self):
        body1 = CelestialBody("N",6e24,Vector(0,0,0),self.zero,self.zero)
        body2 = CelestialBody("M",1e3,Vector(1e7,0,0),Vector(0,3e8,0),self.zero)
        system = System("Dual Body", [body1,body2])
        distance = 1e7
        for _ in range(1,101):
            system.update(1)
            new_distance = CelestialBody.calcDistance(body1,body2)
            self.assertTrue(new_distance > distance)
            distance = new_distance

    def test_ShouldKeepASmallBodyInOrbitWhenTravellingAtOrbitalVelocity(self):
        body1 = CelestialBody("N",5.97219e24,Vector(0,0,0),self.zero,self.zero)
        body2 = CelestialBody("M",1e3,Vector(6.57814e6,0,0),Vector(0,7820,0),self.zero)
        system = System("Dual Body", [body1,body2])
        distance = 6.57814e6
        """for ts in range(1,10*60*1000):
            system.update(0.1)
            new_distance = CelestialBody.calcDistance(body1,body2)
            new_speed = body2.calcSpeed()
            if ts % 600 == 0:
                print("t={}, r={}, v = {}".format(ts/10, new_distance, new_speed))
            self.assertTrue(system.nearly_equal(distance,new_distance,0))
            distance = new_distance"""

    def test_ShouldMoveThreeBodiesOfEqualMassTowardsCenterOfMass(self):
        body1 = CelestialBody("N",6e24,Vector(0,10e10,0),self.zero,self.zero)
        body2 = CelestialBody("M",6e24,Vector(-6e10,-8e10,0),self.zero,self.zero)
        body3 = CelestialBody("L",6e24,Vector(6e10,-8e10,0),self.zero,self.zero)
        system = System("Tri-body", [body1,body2,body3])
        system.update(1)
        self.assertTrue(Vector.sumOfVectors([body1.velocity, body2.velocity,body3.velocity]) == Vector(0,0,0))
        self.assertTrue(Vector.absolute(body1.position) == Vector.absolute(body2.position))
        self.assertTrue(Vector.absolute(body1.position) == Vector.absolute(body3.position))

    def test_      
            

   
if __name__ == '__main__':
    unittest.main()
