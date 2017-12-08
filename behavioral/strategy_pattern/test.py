from strategy.order import Order
from strategy.shipping_cost import ShippingCost
from strategy.strategy_fedex import FedExStrategy
from strategy.strategy_postal import PostalStrategy
from strategy.strategy_ups import UPSStrategy


order = Order()

# Test Federal Express shipping
fedex_strategy = FedExStrategy()
cost_calulator = ShippingCost(fedex_strategy)
cost = cost_calulator.shipping_cost(order)
assert cost == 3.0

# Test UPS shipping
ups_strategy = UPSStrategy()
cost_calulator = ShippingCost(ups_strategy)
cost = cost_calulator.shipping_cost(order)
assert cost == 4.0

# Test Postal Service shipping
postal_strategy = PostalStrategy()
cost_calulator = ShippingCost(postal_strategy)
cost = cost_calulator.shipping_cost(order)
assert cost == 5.0

print('Tests passed')
