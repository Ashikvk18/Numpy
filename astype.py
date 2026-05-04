import numpy as np

arr = np.array([1.1, 2.2, 3.3])
print("Original array data type:", arr.dtype)
newarr = arr.astype('i')
print("Original array:", arr)
print("New array:", newarr)
print("Data type of new array:", newarr.dtype)
