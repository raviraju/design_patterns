from .car_abs import AbstractCar

class Sport(AbstractCar):
    @property
    def description(self):
        return 'Sport'

    @property
    def cost(self):
        return 15000.00
