from vector import Vector

class CelestialBody(object):
    def __init__(self, name, mass, position, velocity, acceleration):
        self.name = name
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def __str__(self):
        return "{}: {}kg, {}, {}m/s".format(
            self.name, self.mass, self.position, self.velocity)
        
    @staticmethod
    def _integrate( t, w, dw_dt):
        delta_w = Vector.mult( t, dw_dt)
        new_w = Vector.add( w, delta_w)
        return new_w

    def update(self, time_interval):
        t = time_interval
        u = self.velocity
        a = self.acceleration
        s = Vector.add(Vector.mult(t,u), Vector.mult(0.5*t*t,a))
        self.position = Vector.add(s, self.position)

        v = Vector.add(u, Vector.mult(t,a))
        self.velocity = v

    def updateWithAcceleration(self, time_interval, acceleration):
        self.acceleration = acceleration
        self.update(time_interval)

    def calcSpeed(self):
        speed = Vector.absolute(self.velocity)
        return speed

    def calcMomentum(self):
        return Vector.mult(self.mass,self.velocity)
    
    def calcKineticEnergy(self):
        velocity_squared = Vector.dot(self.velocity,self.velocity) 
        return 0.5 * self.mass * velocity_squared
        
    
    @staticmethod
    def calcDistance(body1,body2):
        distance = Vector.absolute(Vector.subtract(body2.position,body1.position))
        return distance

 
        
