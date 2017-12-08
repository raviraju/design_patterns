from adapter_abs import AbstractAdapter

class VendAdapter(AbstractAdapter):
    @property
    def name(self):
        return self._adaptee.name

    @property
    def address(self):
        return '{} {}'.format(
            self._adaptee.number,
            self._adaptee.street
        )