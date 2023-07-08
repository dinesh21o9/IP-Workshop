import numpy as np

# print the following 2d matrix.
#  [1 1 1 1 1]
#  [1 0 0 0 1]
#  [1 0 9 0 1]
#  [1 0 0 0 1]
#  [1 1 1 1 1]


a=np.full((5,5),1)

a[1:4,1:4]=0
a[2,2]=9

print(a)


