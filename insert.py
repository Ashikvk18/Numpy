import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Inserting an element
print(np.insert(arr, 2, 10))


print("\n")
print("2D Array")
# 2d array
arr_2d = np.array([[1, 2], [3, 4]])
print(arr_2d)

# Inserting an element
print(np.insert(arr_2d, 1, 10))

# Inserting an element at a specific position
print(np.insert(arr_2d, 1, 10, axis=1)) # axis=1 means column so it will insert 10 in the first column
print(np.insert(arr_2d, 0, 10, axis=0)) # axis=0 means row so it will insert 10 in the first row
print(np.insert(arr_2d, 0, 10, axis=None)) # axis = none means flattening
