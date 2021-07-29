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

#FLOATING POINT NUMBERS:
#there is a problem in the conversion of he floating points with:
x = 0.1 + 0.2
print(x)
print('{0:b}'.format(258)) #cannot format floating point


a = 0.125
divmod(a*2,1)
# (0.0, 0.25) is the output
# here the first item is the quotient whilst th second is the reminder
#given the problem of 0.1+0.2, we can approximate the floating point with the following algorithm:

a = 0.1
bits = []
while a>0:
    q,a = divmod(a*2,1)
    bits.append(q)

b=''.join(['%d'%i for i in bits])
1+sum([int(i)/(2**n) for n,i in enumerate(b,1)]) #thus 0.1 is now equal to = 1.60000023841 x 2^-4
#and for 0.2 = 1.600000002... and we then add the two numbers in binary
#numpy does the same in a much easier way:
import numpy as np
print('%0.12f'%(np.float128(0.1)+np.float128(0.2))) #which converts first the float to binary, sums the binary and gives it back
x = np.float64(0.1)+np.float64(0.2) #if we use more bits (thus not 32 but 64, or not 64 but 128 we get more and more precise results)
y = 0.1+0.2
print(y)
print(x-y)


#MATPLOTLIB:
import matplotlib.pyplot as plt
plt.plot(range(10))
plt.show() #this becomes unnecessary in IPython 
#in a normal interpreter when plotting you the intepreter stops you from using the console
#on the other hand IPython solves this problem
#artists are the figures shown
#canvas is what mpl plots on

# # Note that you can find
# the defaults for Matplotlib in the matplotlib.rcParams dictionary.

#PANDAS -- some knowledge:
#we can specify the indexes to a specific series:
import pandas as pd
x = pd.Series( index = ['a','b','c','d','e','f','g','h','i','l',], data = range(10)) #[0,1,2 ...]
x
type(x)

#we can select data in the series specifying the index with the dot method
x.c
#output: 2
type(x.c) # --> numpy,
#otherwise you can use the .iloc method which permits the spiecification of the data and slicing
x.iloc[:3]
#or by specifying the indexes themselves with the use of .loc method (location)
x.loc['a':'d']

#grouping of data
#data can be grouped with pandas in the following way:
import pandas as pd
x = pd.Series(range(5), [1,2,11,9,10]) #where the data is by default specifies in the first arg of the func series
#moreover the data must be adequate for the groupby
grp = x.groupby(lambda a: a%2) #specifies for which values to groupby, in our case group by based on the fact that they are even
grp.get_group(0) #gets the first group, thus the one specifies
grp.get_group(1) #get the second group, thus the one which we did not specify
grp.max() #gets the maximum value of each group

#DATAFRAME:
#creates a spreadsheet type of frame, encapsulating the series and making them in two dimensions:
import pandas as pd
df = pd.DataFrame({'col1':range(5),
                   'col2':range(5,10)})
df.iloc[:2,:2] #gets the selection
df['col1'] #indexing --> the indexing is given by 0,1,2 ... integers and the indexing of the matrix is given by the colon title
df.col1 # we can use the dot method
#we can use operations on the columns such as the following example:
df.sum() #will sum each column --> yet it wont modify the structure of the dataframe
print(df) 

#group by function with the df
import pandas as pd
df = pd.DataFrame({'col1': [1,1,0,0], 'col2': [1,2,3,4]})
grp = df.groupby('col1') #since there are only two unique entries, we can group by them
grp.get_group(0) #get group grouped by the lowest value identified in the col1 series --> output: 3 & 4
grp.get_group(1) #get the second group --> output: 1 &  2 
grp.sum() #sum the values of each group --> output: 7 & 3
#df can create new columns based on the evaluation of other columns
df['sum_col'] = df.eval('col1+col2') #sums each row into a new column cell
df
#you can group based on multiple columns:
grp = df.groupby(['sum_col','col1'])
res = grp.sum()
res
#output
"""
sum_col col1
2       1        1
3       0        3
        1        2
4       0        4
"""
#for the first row: 2 1 1 indicates: for sum_col = 2 ad for all values for col1 
# For the next row, the same pattern applies except that for sum_col=3, there are
# now two values for col1, namely 0 and 1, which each have their corresponding two
# values for the sum operation in col

#SIMPY
#very useful algebra package
import sympy as S
x = S.symbols('x') #creates a variable for a function
p = sum(x**i for i in range(3)) #creates a poluynomial function
p
type(x)
#we can now solve and find the roots of the function
S.solve(p) #solves for p==0 --> output as list
S.roots(p) #solves for p==0 --> output as  a dictionary
from sympy.abc import a,b,c #quick way to get common symbols
p = a* x**2 + b*x + c
S.solve(p,x) #specific solving for x-variable
#we can use the SImpy exponential for immaginary or complex formulas:
S.exp(S.I*a)
S.expand_complex(S.exp(S.I*a))

#a good integration option is that of computing complicated expressions with Numpy once built with Sympy:
import numpy as np
import sympy as S
y = S.tan(x) * x + x**2
yf = S.lambdify(x,y,'numpy')
y.subs(x,.1) #evaluated using Sympy
yf(.1) #evaluatd using Numpy 
yf(np.arange(3)) #we can now use numpy arrays and output arrays containing multiple solutions to the given function for y = [1,2,3]

# PERFORMANCE AND PARALLEL PROGRAMMING
# #see where a program consumes:
# Python has its own built-in profiler cProfile you can invoke from the command
# line as in the following:
"""python -m cProfile -o program.prof my_program.py"""
# The output of the profiler is saved to the program.prof file. This file can be visual-
# ized in runsnakerun to get a nice graphical picture of where the code is spending
# the most time. The task manager on your operating system can also provide clues as
# your program runs to see how it is consuming resources. 


#NOT POSSIBLE WITH JUPYTER --> USEFUL WITH TERMINAL
# The basic template for using multiprocessing is the following:
# filename multiprocessing_demo.py
import multiprocessing
import time
def worker(k):
    '''worker function'''
    print('am starting process %d' % (k))
    time.sleep(10) # wait ten seconds
    print('am done waiting!')
    return

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=worker, args=(i,))
    p.start()
# Then, you run this program at the terminal as in the following:
# Terminal> python multiprocessing_demo.py
#PAGE 36 FOR OTHER MULTIPROCESSING - JOS UNPINGCO - PYTHON FOR PROBABILITY, STATISTICS AND MACHINE LEARNING 2012

#EVERYTHING ELSE IS ON THE NOTEBOOK






























