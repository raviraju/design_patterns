from strategy.strategy_abc import AbstractStrategy

class FedExStrategy(AbstractStrategy):
    def calculate(self, order):
        return 3.00