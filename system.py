from celestial_body import CelestialBody
from vector import Vector


class System(object):
    def __init__(self, name, bodies):
        self.name = name
        self.bodies = bodies

    def update(self,time_interval):
        accelerations = [calcAcceleration(body) for body in self.bodies]
        for body,acceleration in zip(self.bodies,accelerations):
            body.updateWithAcceleration(time_interval,acceleration)
        

    def calcAcceleration(self,body):
        a_total == 0
        for other_body in self.bodies:
            r_vec = Vector.subtract(other_body.position,body.position)
            r = Vector.absolute(rvec)
            if r == 0.0:
                continue
            m = other_body.mass
            G = 6.67430e-11

            a_vec = Vector.mult(G*m/r**3, r_vec)

            a_total = Vector.add( a_total, a_vec)
        return a_total
            
            
            
    
            
        
