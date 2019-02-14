
import math
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self,v):
        sum = [i+j for i,j in zip(self.coordinates,v.coordinates)]
        return Vector(sum)

    def __add__(self,v):
        return self.plus(v)

        
    def minus(self,v):
        sub = [i-j for i,j in zip(self.coordinates,v.coordinates)]
        return Vector(sub)

    def __sub__(self,v):
        return self.minus(v)

        
    def times_scalar(self,a):
        smul = [i*a for i in self.coordinates]
        return Vector(smul)
        
    def magnit(self):
        sum=0
        for e in self.coordinates:
            sum = sum + e*e
        mag = math.sqrt(sum)
        return mag
    
    def norm(self):
        try:
            mag = self.magnit()
            return self.times_scalar(1/mag)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the Zero vector')
            
    def dot(self,v):
        # v.w = ||v|| * ||w|| * cos(Theta) . where Theta is the short angle between two vectors origin from single point => |v.w| <= ||v|| . ||w|| . 
        # if v.w = ||v|| * ||w|| , then the vectors are in the same direction (cos(0)=1). if v.w=-||v||*||w||, it means the vectors are exactly on the opposite direction (cos(180)=-1). if v.w=0 then either one of the vector is 0 or the vectors are 90 degree ( cos(90) =0 )
        # v.w = v1*w1 + v2*w2 + v3*w3 +... 
        dotv = [i*j for i,j in zip(self.coordinates,v.coordinates)]
        return sum(dotv)
    def angle_with(self,v,in_degree=False):
        # use the above formulas
        dot_with = self.dot(v)
        mag_self= self.magnit()
        mag_v = v.magnit()
        if(mag_self>0.01 and mag_v>0.01):
            angle = math.acos(dot_with/(mag_self*mag_v))
        else:
            print('one of the vectors is 0 vector')
            return 0
            
        if(in_degree):
            return int(angle*180./math.pi)
        else:
            return angle
            
       
    def is_parallel(self,v):
        # two vectors are parallel if the angle between them is 0 or 180
        angle = self.angle_with(v,in_degree=True)
        if(angle<1 or angle >=179):
            return True
        else:
            return False
        
        
    
    
a = Vector([8.218,-9.341])
b = Vector([-1.129,2.111])


print (a+b)

a = Vector([-0.221,7.437])

print( a.magnit())
print(a.norm().magnit())

a = Vector([8,9])
b = Vector([2,-2])

print(a.dot(b))

#a = Vector([0,0])
#print(a.norm())
a= Vector([1,1])
b= Vector([-1,-1])

print(a.angle_with(b,1))
print(a.is_parallel(b))



