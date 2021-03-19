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
for ii in range(10) :
    print('hello')

#il piu uno di ii si aggiunge in automatico
#to graph a square:

# a function can be called by anotherr function, in which case creates a function object.
#for example:
def print_spam(): #the function that will be plugged in
    print('spam')

def do_twice(f): #the function that will repeat the other function
    f() #parenthesis are necessary
    f()

do_twice(print_spam)

#the result is the repetition of the function.



#now lets combine the functions and the turtle module
import turtle
import time
bob = turtle.Turtle()
alice = turtle.Turtle()

def square (t):
    for i in range(4):
        t.fd(100)
        t.lt(90)


def square2 (t):
    for i in range(4):
        t.back(100)
        t.rt(90)

square2(alice)
time.sleep(1)
square(bob) #the second one does not run on the same canvas for some reason

#now lets add a generalization to the square itself.
#specifing exactly the size of the square each time.
import turtle
bob = turtle.Turtle()

def shape(t , degrees, lenght,number_of_sides):
    for i in range(number_of_sides):
        t.fd(lenght)
        t.rt(degrees)

square(bob(),1,2  ,500)

#in this case settings are made in a way for it to create a circle
#now lets change this to any polygon

import turtle
bob = turtle.Turtle()

def polygon(t,n,lenght):
    angle = 360/n
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)

polygon(bob, 7 , 70)

#now lets design a cirlce but still using the function polygon nested in a new function circle

import turtle
import math
bob = turtle.Turtle()
def polygon(t,n,lenght):
    angle = 360/n
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)

def circle(t,r):
    circumference=2*math.pi*r
    n=50
    lenght = circumference
    polygon(t,n,lenght) #i can recall the polygon function inside this function with other parameters

circle(bob, 30)


#to generate ann arch we can refactor, thus make a code more reusable

#to develop adn improvise a program go like this:
#1. start by writing a small program with no function definitions
#2. identify coherent pieces of the program, encapsulate in functions and given names
#3. generalize the function by adding parameters
#4. do the steps 1-3 up until you have generalized all
#5. look for opportunities to refactor.




#DOCSTRING
#it is a string at the beginning of a function that explains the interface
#all doc strings are triple-quoted string, which means that are multiline
#it is used to explain each parameter and what does the function do, without too much details
#it is important for the interface design


######################
#CONDITIONALS
#Floor division and Modulus:
#the floor is an operator which divides a certain number and drops down the fractional part of the result:

minutes = 105
minutes / 60 #would result in 1.75
minutes // 60 #equals 1

#the remainder comes with the modulus operator.
remainder = minutes % 60

#useful ideas with the modulus:

#BOOLEAN EXPRESSIONS:
5 == 6 #compares two things --> false
5 == 5 # --> true
type(True)
#will return 'bool'
#other op:
x != y
x > y
x < y
x >= y
x <= y
#Logical operators:
#and
#or
#not

x > 0 and x < 10
x > 0 or x < 10 #gives true if both are true or just one
#the not operator negates a boolean expression.
#suppose that:
p = 5
l = 6
not p < l #it will return false despite being true
not p > l #it will return true despite being false

#CONDITIONAL STATEMENT
#first type
x = 5 
if x > 0:
    print('x is positive and is:',x)

#the pass statement does not do anything
x = 5 
if x > 0:
    pass

#second of if statement - including an alternative execution
x = 5

if x % 2 == 0:
    print(x, 'is even')
else:
    print(x, 'is odd')

#chained conditionals in which there are more than two possibilites
#we use additional the elif statement
x = 6
y = 7 

if x < y:
    print(y, ' is greter than ' , x)
elif x > y:  #ELIF statement
    print ( x, 'is greater than', y)
else:
    print(x, ' and ', y, ' are eequal' )

#we can chain more than one elif
#the elif s will be checked in order, if the first is false the next is checked
#on the other hand we can use nested conditions
#they are much less readable, so avoid them

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

#rather than having to use the and log-op we can use the if function
#and make an interval comparison

if 0 < x < 10:
    print('x is a positive single-digit number.')



############################
#RECURSION
#it is legal for a function to call another and even to call itself.
#it is 'magical'
#for example:
import time
def countdown(n):
    if n <=0:
        print('blastoff')
    else:
        print(n)
        time.sleep(1)
        countdown(n-1)

#GENIUS

countdown(10)
#a function calling itself is recursive, and computes a recursion
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)
#another example of a recursive, it prints a certain number of times a given string.
#pag101

