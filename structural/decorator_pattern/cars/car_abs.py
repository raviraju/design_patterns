from abc import ABC, abstractproperty

class AbstractCar(ABC):
    @abstractproperty
    def description(self):
        pass

    @abstractproperty
    def cost(self):
        pass
