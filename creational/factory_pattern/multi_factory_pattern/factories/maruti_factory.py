from .abs_factory import AbsFactory
from autos.maruti import MarutiCar

class MarutiFactory(AbsFactory):

    def create_auto(self):
        self.maruti_car = maruti_car = MarutiCar()
        maruti_car.name = 'Maruti Car'
        return maruti_car
