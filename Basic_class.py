class Employee(object):
    'THis is employee base class'
    __empcount = 0
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        print 'init Employee'
        Employee.__empcount += 1
    def __str__(self):
        return "Emp name {} and age is {}".format(self.__name,self.__age)
    def GetEmpCount(self):
        return Employee.__empcount
    def __del__(self):
        Employee.__empcount -= 1
class Manager(Employee):
    def __init__(self,name,age,manpower):
       Employee.__init__(self,name,age)
       self.__manpower = manpower
    def __str__(self):
        return Employee.__str__(self)+" manpower: "+str(self.__manpower)
        
if __name__ == '__main__':
   e1 = Employee('deepak',24)
   print Employee.__doc__
   e2 = Employee('deepakkumar',25)
   print e2
   #print e2.GetEmpCount()
   del e1
   #print e2.GetEmpCount()
   M1 = Manager('shankar',45,13)
   print M1
   print 'Manager has these methods',dir(Manager)