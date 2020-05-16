import unittest

from vector import Vector

class TestVector(unittest.TestCase):
    def setUp(self):
        self.nonZero = Vector (3,4,5)
 
    def test_ShouldEqVectorToSelf(self):
        self.assertTrue( self.nonZero == self.nonZero )

    def test_ShouldNotNeVectorToSelf(self):
        self.assertFalse( self.nonZero != self.nonZero )

    def test_ShouldAddTwoVectors(self):
        self.assertTrue( Vector.add(self.nonZero, Vector(7,1,2) ) == Vector(10,5,7) )

    def test_ShouldDotTwoVectors(self):
        self.assertTrue( Vector.dot(self.nonZero, Vector(2,3,5) ) == 43)
        
    def test_ShouldMultScalarAndVector(self):
        self.assertTrue( Vector.mult(2,self.nonZero) == Vector (6,8,10))

    def test_ShouldFindModOfVector(self):
        self.assertTrue( Vector.absolute(Vector(1,2,2)) == 3)
       
if __name__ == '__main__':
    unittest.main()
