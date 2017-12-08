from adapter_abs import AbstractAdapter

class CustAdapter(AbstractAdapter):
    @property
    def name(self):
        return self._adaptee.name

    @property
    def address(self):
        return self._adaptee.address
        