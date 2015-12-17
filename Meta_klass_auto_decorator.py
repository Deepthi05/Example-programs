import inspect
class AutoDecorateMeta(type):
    def __init__(cls, name, bases, ns):
        deco = ns.get('decorator', lambda f: f)
        for key, value in ns.items():
            # skip the decorator and constructor
            if key in ('decorator', '__init__'): continue

            # skip objects in the namespace that aren't methods
            if not inspect.isfunction(value): continue

            # apply the decorator
            setattr(cls, key, deco(value))
class Person(object):
        __metaclass__ = AutoDecorateMeta
        decorator = property

        def __init__(self, first, middle, last):
            self.first = first
            self.middle = middle
            self.last = last

        def name(self):
            return '%s %s' % (self.first, self.last)

        def full_name(self):
            return '%s %s %s' % (self.first, self.middle, self.last)

        def initials(self):
            return '%s%s%s' % (self.first[0], self.middle[0], self.last[0])

mlk = Person('Martin', 'Luther', 'King')
print mlk.name
print mlk.full_name
print mlk.initials