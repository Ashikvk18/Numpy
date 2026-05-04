import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# Flattening
print(arr.flatten()) # it means 1D array

# ravel
print(arr.ravel()) # it means 1D array

# difference between flatten and ravel
# flatten returns a copy of the array
# ravel returns a view of the array

# difference between copy and view: copy can be modified without affecting the original array 
# view is a reference to the original array so it will affect the original array