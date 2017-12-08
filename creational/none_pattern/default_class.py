from abs_class import AbstractClass

class DefaultClass(AbstractClass):
    def do_something(self, value):
        print('By default, Not doing %s.' % value)