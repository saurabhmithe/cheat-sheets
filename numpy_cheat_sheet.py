import numpy as np

# using numpy instead of lists
# saves programming time using pre-defined functions
# uses a single datatype for each element in the array
# the library functions are efficient and written for performance
# uses contiguous blocks of memory
# numpy array vs normal list = java array vs linked list

list = [1, 2, 3]
print(list)

# repeats the list 3 times
# list = list * 3
# print(list)

np_list = np.array(list)
print(np_list)
# multiplies each element of the list by 3
np_list = np_list * 3
print(np_list)

# make an np array from a list
a = np.array([1, 2, 3])
print(a)

# make an np array by specifying a range start_end_step
a = np.arange(1, 12, 3)
print(a)

# make an np array with n evenly spaced elements in a range
a = np.linspace(1, 12, 6)
print(a)

# reshape an array into a 2-d array or a matrix
# creates 3 rows of 2 elements each and returns the new array
a = a.reshape(3, 2)
print(a)

n = np.arange(1, 13, 1)
print(n)
n = n.reshape(4, 3)
print(n)

# size of the array regardless of the shape
print(n.size)

# shape of the array
print(n.shape)

# datatype of the elements in the array
print(n.dtype)

# memory in bytes of each array element
print(n.itemsize)

b = np.array([(1, 2, 3), (4, 5, 6)])
print(b)

# compares each element with 3 and returns an array of each individual result
m_b = b <= 3
print(m_b)

s_b = b * 3
print(s_b)

# create an empty array full of zeros default to float64
z = np.zeros((3, 3))
print(z)

# create an empty array full of ones default to int16
o = np.ones((3, 3), dtype=np.int16)
print(o)

# create an array with random values from 0 to 1
r = np.random.random((3, 3))
print(r)

# set print options for all the future print statements
np.set_printoptions(precision=2, suppress=True)
print(r)

# create an array with random integers in the specified range
r_int = np.random.randint(0, 10, 9)
r_int = r_int.reshape(3, 3)
print(r_int)

arr = np.arange(1, 101, 1)
print(arr)
print(arr.min())
print(arr.max())
print(arr.mean())
print(arr.var())
print(arr.std())

mat = np.random.randint(1, 10, 6)
mat = mat.reshape(3, 2)
print(mat)
print(mat.sum(axis=1))  # sum of elements along y axis
print(mat.sum(axis=0))  # sum of elements along x axis