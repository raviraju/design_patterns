from cars.car_economy import Economy
from decorators.decor_v6 import V6
from decorators.decor_vinyl import Vinyl
from decorators.decor_black import Black

def main():
    car = Economy()
    show(car)
    car = V6(car)
    show(car)
    car = Vinyl(car)
    show(car)
    car = Black(car)
    show(car)

def show(car):
    print('Description: {}; cost: ${}'.format(car.description, car.cost))

if __name__ == '__main__':
    main()
