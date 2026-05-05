import numpy as np

# first with loops

prices = [10, 20, 30, 40, 50]
discount = 10
final_prices = []
for price in prices:
    final_price = price - (price * discount / 100)
    final_prices.append(final_price)
print(final_prices)


# now with numpy

prices = np.array([10, 20, 30, 40, 50])
discount = 10
final_prices = prices - (prices * discount / 100)
print(final_prices)

