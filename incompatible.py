import numpy as np

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([1,2])

# print(arr1 + arr2)

#reshape arr2 to match arr1 for broadcasting
arr2 = arr2.reshape(2,1)
print("Reshaped arr2:", arr2)
print("Result after addition:", arr1 + arr2)