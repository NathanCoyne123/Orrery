import math

class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return str(self.x) + "i + " + str(self.y) + "j + " + str(self.z) + "k"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    @staticmethod
    def add(a,b):
        X = a.x + b.x
        Y = a.y + b.y
        Z = a.z + b.z
        return Vector(X,Y,Z)
    
    @staticmethod
    def subtract(a,b):
        X = a.x - b.x
        Y = a.y - b.y
        Z = a.z - b.z
        return Vector(X,Y,Z)

    @staticmethod
    def dot(a,b):
        return a.x * b.x + a.y * b.y + a.z * b.z
    
    @staticmethod
    def mult(scalar,vector):
        X = scalar * vector.x 
        Y = scalar * vector.y 
        Z = scalar * vector.z 
        return Vector(X,Y,Z)

    @staticmethod
    def absolute(vector):
        mod_squared = Vector.dot(vector,vector)
        return math.sqrt(mod_squared)

    @staticmethod
    def angle(a,b):
        dot_ab = Vector.dot(a,b)
        abs_a = Vector.absolute(a)
        abs_b = Vector.absolute(b)
        print ("a.b={},|a|={},|b|={}".format(dot_ab, abs_a, abs_b))
        return math.acos(dot_ab / (abs_a * abs_b))

    
"""    
a = Vector(10,7,10)
b = Vector(1,1,1)



print (a)
print (b)
    
print(Vector.add(a,b))
print(Vector.dot(a,b))
"""
