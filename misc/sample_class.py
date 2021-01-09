class SampleClass:

    def __init__(self, a):
        ## private varibale or property in Python
        self.__a = a
        self.__b = '123'

    ## getter method to get the properties using an object
    def get_a(self):
        return self.__a

    ## setter method to change the value 'a' using an object
    def set_a(self, a):
        self.__a = a

if __name__ == "__main__":
    simple1 = SampleClass('xyz')
    simple1.__a = 'abc' # not error
    print(simple1.__a)#abc
    #print(simple1.__b)#AttributeError: 'SampleClass' object has no attribute '__b'
    simple1.c = 'ccc'
    print(simple1.c)#ccc
    print(simple1.get_a())# xyz
    print(simple1)
    simple2 = SampleClass('xyz')
    simple2.set_a('abc')
    print(simple2.get_a())# abc