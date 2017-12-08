from cars.car_abs import AbstractCar

class AbstractDecorator(AbstractCar):
    def __init__(self, car):
        self._car = car

    @property
    def car(self):
        return self._car
