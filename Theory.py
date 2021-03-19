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

def new_fnct(): #the header of the function is meant to have the colon
    print(' this is the test for a new function')
    print('how are you doing')

      #to end the function just leave an empty line


#def indicates that what follows is the definition of the function
#the name of the f is 'new_fnct'
#the first line of the function is the header
#the rest of it is the body

#to recall a function is like to recall any other function package
new_fnct()


def function_two():
    print(2+2)
    print(math.pi)

function_two



#this will in the first step create a function and then recall it
#to run a code it is important to know the flow of execution
#thus always use a scheme

#parameters and arguments

math.sin
#sin requires an argument to the function itself
#we want to create functions that have arguments
#inside a function the argument is assigned to a variable, called paramenter

def pyt(zz):
    print(zz)
    print(zz)

#this function prints out the variable zz twice, where zz is the paramenter
#so if i call the function with that given parameter it will perform the set of commands
#with the argument inserted

pyt(math.pi)

#the argument is evaluated before the function itself
#i can apply any other operation on the value before inserting it
#for example:

pyt('sample'*4)

#as well as you can use other variables as arguments
#variables created within the function and paramenters are local, thus they exist only within the function
#to keep track of the variables it is good to use a stack diagram.
#function that return a value are fruitful, such as math function
#functions that print a value only or do not return it are void functions.


#the function len() gives the length of the string
#never forget about concatenation


#how to check whether you have the turtle module

import turtle
bob = turtle.Turtle()

#the turtle can be moved around.
#the turtle with a lower case t gives a function which  

print(bob)
turtle.mainloop()

#mainloop means that is waiting for the user, but actually there is nothing to do
#once you have created turtle, you can call method to move it around the windows. a method is
#similar to a function but it uses slighly different syntax

#to move the turtle forward use the following method:
import turtle
bob = turtle.Turtle()
bob.fd(4)
print(bob)

#bk will move it bk, lt or rt will make it move to the left and to the right
#Also, each Turtle is holding a pen, which is either down or up; if the pen is down, the
#Turtle leaves a trail when it moves. The methods pu and pd stand for “pen up” and “pen
#down”. 

bob.pd

#to draw a right corner:
import turtle
bob = turtle.Turtle()
bob.pd()
bob.fd(100)
bob.lt(90)
bob.fd(100)
turtle.mainloop()



#CICLES:
#for a for cycle using the range function:
ii = 1
for i in range(10) :
    print('hello')

#il piu uno di ii si aggiunge in automatico
#to graph a square:
