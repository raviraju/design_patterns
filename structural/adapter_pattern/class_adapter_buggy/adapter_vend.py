from obj_customer import Customer
from obj_vendor import Vendor

class VendAdapter(Vendor, Customer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def address(self):
        return '{} {}'.format(
            self.number, self.street
        )
