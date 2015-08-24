# if container is a list, a + b will concatenate:

list_one = [1,2,3,4,5]
list_two = [6,7,8,9,10]

print(list_one + list_two)

# if container is a numpy array, places will be added:

from numpy import *

a = array([1,2,3,4,5])
b = array((6,7,8,9,10)) # tuple also works. ((6,7))

print(a + b)

c = array([11,12,13,14])


print(c + 100)