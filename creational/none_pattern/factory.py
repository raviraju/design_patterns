from some_class import SomeClass
from default_class import DefaultClass

class Factory:
    @staticmethod
    def create_object(value):
        if value == 'some_class':
            return SomeClass()
        else:
            return DefaultClass()
