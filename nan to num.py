import numpy as np

arr = np.array([1, 2, 3, np.nan, 5])
print(np.nan_to_num(arr))

print(np.nan_to_num(arr, nan=100))
