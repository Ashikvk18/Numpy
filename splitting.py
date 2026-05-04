import numpy as np

# equally split
arr = np.array([1, 2, 3, 4, 5, 6])
print(np.split(arr, 2))

#unequally split
arr = np.array([1, 2, 3, 4, 5, 6])
print(np.split(arr, [1, 3])) # splits at 1 then 2 and then 3


