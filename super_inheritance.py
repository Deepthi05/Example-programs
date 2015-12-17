#####Diamond Problem:: And use of super keyword#######

class BaseClass(object):
  num_base_calls = 0
  def __init__(self):
    object.__init__(self)
    #super(BaseClass,self).__init__()
    print "Init Base"
  def call_me(self):
    print("Calling method on Base Class")
    self.num_base_calls += 1

class LeftSubclass(BaseClass):
  num_left_calls = 0
  def __init__(self):
    BaseClass.__init__(self)
    #super(LeftSubclass,self).__init__()
    print "Init Left Subclass"
  def call_me(self):
    #BaseClass.call_me(self)
    super(LeftSubclass,self).call_me()
    print("Calling method on Left Subclass")
    self.num_left_calls += 1

class RightSubclass(BaseClass):
  num_right_calls = 0
  def __init__(self):
    BaseClass.__init__(self)
    #super(RightSubclass,self).__init__()
    print "Init Right SubClass"
  def call_me(self):
    #BaseClass.call_me(self)
    super(RightSubclass,self).call_me()
    print("Calling method on Right Subclass")
    self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
  num_sub_calls = 0
  def __init__(self):
    LeftSubclass.__init__(self)
    RightSubclass.__init__(self)
    #super(Subclass,self).__init__()
    print "Init Subclass"
  def call_me(self):
    #LeftSubclass.call_me(self)
    #RightSubclass.call_me(self)
    super(Subclass,self).call_me()  
    print("Calling method on Subclass")
    self.num_sub_calls += 1

s1 = Subclass()
s1.call_me()