import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Slicing
print(arr[1:4]) # start : end = 1 to 3 (4 is excluded) indices
print(arr[:3]) # start : end = 0 to 2 (3 is excluded) indices
print(arr[3:]) # start : end = 3 to 4 (5 is excluded) indices
print(arr[-3:-1]) # start : end = -3 to -2 (-1 is excluded) indices
print(arr[::2]) # start : end : step = 0 to 4 (5 is excluded) indices with step 2
print(arr[1::2]) # start : end : step = 1 to 4 (5 is excluded) indices with step 2
print(arr[::-1]) # start : end : step = 4 to 0 (0 is excluded) with step -1
print(arr[::-2]) # start : end : step = 4 to 0 (0 is excluded) with step -2

