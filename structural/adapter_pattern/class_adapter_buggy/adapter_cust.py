from obj_customer import Customer

class CustAdapter(Customer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)