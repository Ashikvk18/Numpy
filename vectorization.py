import numpy as np
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

print([x+y for x,y in zip(list1,list2)])

arr1 = np.array(list1)
arr2 = np.array(list2)

print(arr1 + arr2)