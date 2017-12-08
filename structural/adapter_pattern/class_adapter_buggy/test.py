from obj_customer import Customer
from adapter_cust import CustAdapter

from obj_vendor import Vendor
from adapter_vend import VendAdapter

MOCKCUSTOMERS = (
    CustAdapter(Customer('Dough Factory', '#1, Semolina Court')),
    CustAdapter(Customer('Farm Produce', '#14, Country Rd.')),
    CustAdapter(Customer('Cocoa World', '#53, Tropical Blvd.'))
)

MOCKVENDORS = (
    VendAdapter(Vendor('Dough Factory', 1, 'Semolina Court')),
    VendAdapter(Vendor('Farm Produce', 14, 'Country Rd.')),
    VendAdapter(Vendor('Cocoa World', 53, 'Tropical Blvd.'))
)

def display(PERSONS):
    for person in PERSONS:
        print('Name: %s; Address: %s' %
              (person.name, person.address))

def main():
    display(MOCKCUSTOMERS)
    display(MOCKVENDORS)

if __name__ == '__main__':
    main()
