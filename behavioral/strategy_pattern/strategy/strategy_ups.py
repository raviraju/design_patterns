from strategy.strategy_abc import AbstractStrategy

class UPSStrategy(AbstractStrategy):
    def calculate(self, order):
        return 4.00