import numpy as np

# creating an array with numpy arrays
arr = np.array([1, 2, 3, 4, 5])

print(arr,end="\n\n")

# accecing arrays using array indexing
print(arr[0] ,end="\n\n")

# array slicing
print(arr[1:3],end="\n\n")

# array copy method for copying arrays
copyarr = np.copy(arr)

arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
np.shape(arr2)
print(arr2,end="\n\n")

# storing 1 to 6 arrays
a = np.arange(6)
print(a,end="\n\n")

# reshaping array with new dimensions
b = a.reshape(3, 2)
print(b,end="\n\n")

# summing the columns
b.sum(axis=0)
print(b.sum(axis=0),end="\n\n")
