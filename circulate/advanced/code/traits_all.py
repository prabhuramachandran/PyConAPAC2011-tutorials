from enthought.traits.api import Delegate, HasTraits, Int, Str, Instance

class Parent(HasTraits):
    # INITIALIZATION: 'last_name' initialized to ''
    last_name = Str('') 

class Child(HasTraits):
    age = Int
    # VALIDATION: 'father' must be Parent instance
    father = Instance(Parent)
    # DELEGATION: 'last_name' delegated to father's 
    last_name = Delegate('father') 
    # NOTIFICATION: Method called when 'age' changes
    def _age_changed(self, old, new): 
        print 'Age changed from %s to %s ' % (old, new)
