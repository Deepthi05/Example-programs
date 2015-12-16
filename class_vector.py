class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      print "im in add"
      return Vector(self.a + other.a, self.b + other.b)
   def __sub__(self,other):
      return Vector(self.a - other.a, self.b - other.b)
   def __mul__(self,other):
      return Vector(self.a * other.a, self.b * other.b)
   
   def __radd__(self,other):
      return Vector(self.a + other, self.b + other)
     
   
v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2
print v1.__add__(v2)
print Vector.__add__(v1,v2)
print v1 * v2
print 'calling +='
v1 += v2
print  v1
#print v1 + 1
#print v1.__add__(1

#print  1 + v1
#print v1.__add__(v2)
#print Vector.__add__(v1,v2)
#print v1 - v2
#print v1 * V2 # __mul__
#print v1 / v2 # __div__ 
Status API Training Shop Blog About Pricing
© 2015 GitHub, Inc. Terms Privacy S