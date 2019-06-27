# pynumber: 2
# create a numpy array of  8x2 as having number  
# in each cell between 100 and 200 
# such that difference between each element is 5  

import numpy as np
mylist=np.arange(100,200,5)
print(mylist)
mylist = mylist[0:16].reshape(8,2)
print(mylist)