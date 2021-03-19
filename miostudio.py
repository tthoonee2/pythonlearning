import math #mathematical library for mathematical functions
message = ' and now something completely different'
n = 17
pi = 3.141592

print(message)
print(n*pi)
#this is basically a comment

#and the following is a concatenation
print('lorem' + ' ipsum')

#there are three types of errors:
#syntax
#runtime - usually exceptions 
#semantic - semantic prbelm wont give error meessages but wont do the right thing

x = y = 1
print(x,y)

#################################
#useful functions
type(x) #returns the value of x
int(x) #takes in the value of x and tries to convert it to an integer
float(x) #takes in the value of x and tries to convert it to a float
str(x) #take in the value of x and tries to convert it to a string

math #gives out more information about math 's statement
#to access the functions within the module (math) you use the following syntax

signal_power = 1100
noise_power = 100000
ratio = signal_power / noise_power
decibel = 10*math.log10(ratio) #we see here the use of the module and the function
print(decibel)
 #another example

 radians = 0.7
 height = math.sin(radians)
 print(height)

#the expression
pi = math.pi #is the pi number
print(pi)

###################################


#setting up a function

def new_fnct():
    print(' this is the test for a new function')
    print 'how are you doing'

#def indicates that what follows is the definition of the function
#the name of the f is 'new_fnct'
#se faccio una modifica chissa se viene fuori