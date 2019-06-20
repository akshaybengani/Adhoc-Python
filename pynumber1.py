# create 2D numpy  based array with given conditions:
# i)   take input from user in terms of dimension like (3x2 or 6x7)
# ii)   fill this numpy array with random number
# iii)  store this array in a file

import numpy as np
mylist = np.random.randint(10,size=(3,2))

print(mylist)
fhand = open('randomArray.txt','w+')
fhand.write(str(mylist))
