#The "Pythonic" way is not to use "getters" and "setters", but to use plain attributes, 
class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        print("getter of x called")
        return self._x

    @x.setter
    def x(self, value):
        print("setter of x called")
        self._x = value

    @x.deleter
    def x(self):
        print("deleter of x called")
        del self._x

class supperc(C):
    
    @C.x.getter
    def x(self):
        return 'super ' + self._x

c = C()
c.x = 'foo-x'  # setter called
foo = c.x    # getter called
print("foo is "+foo) 
del c.x      # deleter called
print("foo is "+foo)#foo is foo-x
#print(c.x) #error

supc = supperc()
supc.x = 'John' #setter of x called 
print(supc.x)#super John
#---output ---
# setter of x called
# getter of x called
# foo is foo-x
# deleter of x called
# foo is foo-x
# setter of x called
# super John

