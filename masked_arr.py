import numpy as np

y = ma.array([1,2,3], mask=[0,1,0])

y[1] is ma.masked
# output True

print(y[1])
# output --

y[-1] = ma.masked

print(y)

# output:
# masked_array(data = [1 -- --],
#              mask = [False  True  True],
#        fill_value = 999999)
