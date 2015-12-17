class Parent(object):        # define parent class
   parentAttr = 100
   def __init__(self,x):
      self.x = x
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self,x,y):
      Parent.__init__(self,x)
      self.y = y
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'
   def print_child(self):
       print self.x,self.y
   def parentMethod(self):
      print 'Calling child method'

c = Child(10,20)          # instance of child
c.childMethod()
c.print_child()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method