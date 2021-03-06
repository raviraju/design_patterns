from transport_bus import Bus
from transport_airplane import Airplane

def main():
    travel('New York', Bus)
    travel('Amsterdam', Airplane)

def travel(destination, transport):
    print(('Taking the {} to {} ' + '=====>').format(
        transport.__name__,
        destination
    ))

    means = transport(destination)
    means.take_trip()

if __name__ == '__main__':
    main()
