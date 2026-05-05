import numpy as np

arr = np.array([1, 2, 3, np.inf, 5])
print(np.isinf(arr))

arr2 = np.array([1, 2, 3, np.inf, 5, -np.inf])
print(np.isinf(arr2))

cleaned_arr = np.nan_to_num(arr, posinf=100, neginf=-100)
print(cleaned_arr)

cleaned_arr2 = np.nan_to_num(arr2, posinf=100, neginf=-100)
print(cleaned_arr2)