class Field(object):
        def __init__(self, ftype):
            self.ftype = ftype
            print "inside feild creation"

        def is_valid(self, value):
            print self.ftype,type(value)
            return isinstance(value, self.ftype)

class EnforcerMeta(type):
        def __init__(cls, name, bases, ns):
            # store the field definitions on the class as a dictionary 
            # mapping the field name to the Field instance.
            cls._fields = {}
            print "Inside EnforceMeta creation"

            # loop through the namespace looking for Field instances
            for key, value in ns.items():
                print "key and value",key,value
                if isinstance(value, Field):
                    cls._fields[key] = value

class Enforcer(object):
        # attach the metaclass
        __metaclass__ = EnforcerMeta

        def __init__(self):
            print "inside Enforcer creation"

        def __setattr__(self, key, value):
            print "inside setattr",key,value
            if key in self._fields:
                print self._fields
                if not self._fields[key].is_valid(value):
                    raise TypeError('Invalid type for field!')
            super(Enforcer, self).__setattr__(key, value)

class Person(Enforcer):
        name = Field(str)
        age = Field(int)
        def __init__(self):
            print "inside Person creation"

print "Before Person creation"
Naveen = Person()
print "After Person creation"
#Naveen.name = 3
#Naveen.age = 'Guy'
Naveen.name = "Steve"
Naveen.age = 30
