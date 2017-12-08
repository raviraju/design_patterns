from abc import ABC, abstractproperty

class AbstractAdapter(ABC):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    @property
    def adaptee(self):
        return self._adaptee

    @abstractproperty
    def name(self):
        pass

    @abstractproperty
    def address(self):
        pass
