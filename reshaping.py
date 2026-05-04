import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)

# Reshaping
print(arr.reshape(3, 2)) # it means 3 rows and 2 columns
# dimension needs to match like `3 * 2 = 6`
# it doesn't change the original array