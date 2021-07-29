#to start
import numpy as np #standard convention to import it as np
x = np.array([1,2,3], dtype=np.float32) #we created an array of floats of 32bits each, which means it has 4 bytes in total
x
x.itemsize #output  the size of the items contained, which are of 4 Bytes thus the output is "4"

#np includes ufuncs --> are used to avoid looping semantics:
y = np.sin(np.array([1,2,3], dtype = np.float32)) #this will provide us with an array of each 32 bits containing the sins of the infedels.
#whereas we would need a for loop with the function given by math
from math import sin
y = [sin(i) for i in [1,2,3]]

#we can build shapes with the lenghts of the arrays:
x  = np.array([[1,2,3], [4,5,6]]) # sort of matrix
x.shape

y = np.array([[1,2],[1,2]]) #the vectors are limited to 32 dimensions
y.shape

#NUMPY SLICING RULES:
#it is equal, the colon selects all the elements on a given axis -- ex:
x  = np.array([[1,2,3], [4,5,6]])
x[:,0] #will select all items from the column 0, which is the first position in the arrays
x[:,1] #will select all items from the column 1, which is the second position in the arrays
x[0,:] #will select all items from the row 0 --> output is [1,2,3]
x[1,:] #will select all items from the row 0 --> output is [4,5,6]
x['rows':'columns'] # --> general rule
# in the last position the step can be specified:
x[:,1:] #--> except first
x[:,::2] # all rows, every other column
x[:,::-1] # reverse order of columns
#slicing is just viewing the array up until you do not specify the re-assignment

#ARRAYs and Memory
import numpy as np
x = np.ones((3,3)) #extends an array, or simply returns a matrix with the specified dimensions --> requires tuple or list
#we can reassign values on an already memorized array
x[0,0] = 12
#to view the top left corner
x[:2,:2] 
#to viw the bottom left corner
x[1:,1:]
#colon gives you the direction of the selection to be viewed

#slices creates view, thus memory is affected if in a variable the view is copied and we modify the initial variable of the view
# we have to force a copying:
x = np.arange(5) # create array with range 
y = x[0,1,2] #selects and copies specific integers --> we force those integers
z=x[:3] # slice creates view
x[0]=999 # change element of x
y # note y is unaffected,
z # but z is (it's a view).
#In this example, y is a copy, not a view, because it was created using advanced
# indexing whereas z was created using slicing

#MATRICES
A = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
x = np.matrix ([1],[0],[0])
A*x
#matrix operations
#for multiplications we can use also the .dot() method
A.dot(x)
#which is the inner vector multiplication
#or for the matrix multiplication in python 3.x you can use @
A @ x
#multiple row arrays are not equal to matrices

#NUMPY BROADCASTING:
X,Y = np.meshgrid(np.arange(2), np.arange(2)) #da riprendere

#NUMPY MASKED ARRAYS:
#the use is to temporarly hide elements from the array without changing the shape of the array itself
from numpy import ma #import maskd arrays
x = np.arange(10)
y = ma.masked_array(x,x<5) #in the first arg we specify which vector to be masked, and in the second arg we specify the condition for 
#which an element should be masked
#we can still interact with the original array
#ex:
from numpy import ma 
import numpy as np
a = np.array([5,6,7,7,7,7,6,5,5,4])
b = ma.masked_array(a, a<6)
print(b)



