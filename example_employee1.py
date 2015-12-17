class Employee(object):
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      'my init method'
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
   def __str__(self):
      return "Name: {0} Age :{1}".format(self.name,self.salary)
'''print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__'''
E1 = Employee('abc',10000)
print E1