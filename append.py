import numpy as np

# 1D array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Appending an element
print(np.append(arr, 6))

print("\n")
print("2D Array")
# 2D array
arr_2d = np.array([[1, 2], [3, 4]])
print(arr_2d)

# Appending an element
print(np.append(arr_2d, 5))

# Appending an element at a specific position
# Need to reshape the scalar to match array dimensions
print(np.append(arr_2d, [[5, 5]], axis=0)) # axis=0 means row so it will append [5, 5] as a new row
print(np.append(arr_2d, [[5], [5]], axis=1)) # axis=1 means column so it will append 5 as new columns
