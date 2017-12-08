from abc import ABC, abstractmethod
from observers import AbstractObserver


class AbstractSubject(ABC):
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbstractObserver):
            raise TypeError('Observer not derived from AbstractObserver')
        self._observers |= {observer}

    def detach(self, observer):
        self._observers -= {observer}

    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._observers.clear()
