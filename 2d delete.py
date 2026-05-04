import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# Deleting an element
new_arr = np.delete(arr, 1, axis=1)
print(new_arr)

new_arr = np.delete(arr, 1, axis=0)
print(new_arr)