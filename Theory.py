# questions are marked as follows: ???



import math
from os import O_APPEND, curdir
from tkinter import Label #mathematical library for mathematical functions
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


###MATHEMATICAL OPERATION:

sum(1,2,3,4) #will sum the values
max(list tuple strings  or integers)
min(list tuple strings  or integers) 


"""
+ #ADDITION
- #subtraction
* #multiplication
/ #division
// #floor division --> divides two numbers and rounds down to an integer --> come quelle che facevi in colonna
% #modulus --> divides two integers and returns the vlaue of the reminddr
** #exponentiation

"""
##FORMATTING:
variable = format(1000.42520902, '.2f') 
format(1000/7, ',.2f')
format(1000/7, ',.2%')
help(format)
help('FORMATTING')

round(3.8879823, 0) #will roundup the number to the specified by the second argument










################################# 
#useful functions
type(x) #returns the value of x
int(x) #takes in the value of x and tries to convert it to an integer
float(x) #takes in the value of x and tries to convert it to a float
str(x) #take in the value of x and tries to convert it to a string

math #gives out more information about math 's module (class) 
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


####FUNCTIONS:
#functions are useFUL to create a modular program

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

function_two()



#this will in the first step create a function and then recall it
#to run a code it is important to know the flow of execution
#thus always use a scheme

#parameters and arguments





math.sin()
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

def anexample(mandatory_parameter, optional_parameter = 2):
    return
''' the optional parameter is always at the end of the declaration of the parameters
the mandatory parameter are always at the beginning'''




#adding optonal arguments
def test(a,b,c, *args, **kwargs):
    print(args)
    print(args[4])
    
    
test(1,2,3,4,4,4,5,6,6)
#and you can iterate the args like a vector as well as the kwargs - ??? lists or dictionaries - ##are tuples too???

#if you want to set default values:
def test2(par1,par2,par3,par4 = 5, par5 = 6):
    #the optionals par4 and par5 have to be put after the mandatory ones, so the defualt, also called optional, always follow the mandatory.

#you can call arguments as you wish
test2(par2= 5, par3= 8)

#we can recall global values internally but not the opposite:
world = 100

def test3():
    return 199-world







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
#Turtle leaves a trail when it moves. The methods pu and pd stand for ???pen up??? and ???pen
#down???. 

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

for ii in range(10): # there is no need to define ii
    print('hello')
    
    
    
    
#Range function:
#the range function returns the object that produces a sequence of integers from start (inclusive), to stop (exclusive) 
# by increments of step:
range(i, j)
#if start is omitted the default value is 0
#the last position of range is not used
range(1,10,2) # starting from 1 going up to 9 stepping by 2 
    

#EXAMPLE:
#Harmonic sum
def harmonic_sum(N, a):
    result = 0
    for n in range(1, N+1):  #range is needed whenever the variable is not iterable
        element = 1 / n**a   #N+1 and starting from 1 (1, N+1)
        result += element

    return result


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

#to develop and improvise a program go like this:
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
and
or
not

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


#we can check if there certain values in a given list in the following way:
rain = 'y'
if rain in ["Yes",'yes','y']:
    print('put on a coat')
#check if the variable rain, containing in this case the value 'y' is present in the list

 




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

###############
#INPUT
text = input()
#this will make the program wait for an input from the user

name = input('what is your name? \n')
#this will display the quesiton and then wait for ani input
#\n is a marker that makes the phrase go on a new line
#it must be a string of digits the input, and you cannot convert it to an integer like that-
#Error:
prompt = ' what is the airspeed velocity of an unladed swallon \n'
speed=input(prompt)
#after the input
int(speed) #sometimes it works for some strange reason - it always does if done correctly

########
#FRUITFUL FUNCTIONS AND RETURN VALUES:
#when i call a mathematical function it will return a value
#up until now we have called and designed void functions
#we are finally returning values.
#example of an area functin







def area (a,b):
    c = a*b
    return c

#or
def area_circle(radius):
    """it gives the area of the circle"""
    a = math.pi * radius**2
    return a

#or to even be more synthetic
def area_circle_2(radius):
    return math.pi * radius ** 2

#even though temporary var such as a can be useful in debugging
#there could be used also with operators such as

#define an input value

number = -69

def absolute_value(x):
    if x < 0:
        return -x
    if x > 0:
        return x

absolute_value(number)

#the part of code which will never be reached by the flow of the program
#is called dead code

#to use less computationla power during the debugging process it is good
#to develop incrementally
#for example if you want to find a distance using the the pythagorean
#theorem you shall start by developing the smallest functions and then increasing it.

####### composition
#you can call one function from the other

###### Boolean functions
#functions that can return booleans, they hide the huge amount of tests from inside of the functions
#for example:

def is_divisible(x,y):
    if x % y == 0:
        return True
    else:
        return False

#vorpal = something which is not useful like a perfectly recursive and uncallable function #-#
#a useful mathematical function could be a factorial function

def factorial(n):
    if n == 0:
        return 1
    else:
        recursive = factorial(n-1)
        result = n*recursive
        return result

factorial(300)

##### Leap of Faith
# instead of checking every single time th eflow of execution we assume that it  works
# we have to check the type of the parameters, arguments and values:
isinstance(n, int) #check the value of the variable n if corrisponds to integer 
if not isinstance(n, int):
    print('insert an integer please')

#this form of check ups are guardians that cann be put at the beginning of functions

####### the while function
# the while statement provides for a more logical and simplified iteration
# while something is l_op wrt to something

#### break
#the break statement gives you the opportunity to jump out of the loop or cycle
#the opposite statement is the continue statement
""" 
    break
    continue
"""







while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Done')
a = 4
#### square roots can be calculated with the newton's method
y=(x+a/x)/2
#where y is the square root, x is the nearest estimate, a is the number to be rooted.
#suppose
a = 4
x = 3
y = ( x + a/x)/2
y

# to approximate even better
a = 56
x = 8


while True:
    print(x)
    y = (x + a/x)/2
    if y ==x:
        break
    x = y

######
#this is an example of algorithm

###SEQUENCES IN COMMON:
#operators:
''' 
+ --> concatenation
* --> repetition and merging
in --> returns true if an element is found in a sequence
len(seq) --> returns the number of elements of the sequence
max(seq) and min(seq) --> returns the largest and the smallest value in a sequence
sorted(seq) --> returns a new list with the elements sorted in ascending order
sum(seq) --> sums the elements of the sequence ( numbers only )

'''
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3) #concatenates

#STRINGS METHODS
#methods:
# .upper() --> returns a copy with all the chars in capital
# .lower() --> returns a copy with all theh chars in lower
# .find() --> returns the index of the the argument of the method in the string
# .startswith() --> returns true if the strings starts with the argument specified in the function
# .endswith() --> returns true if the string starts wit hthe argument specified by the method
# .count() --> returns the number of times the argument is found in the string
# .split() --> splits the string into a list based on the value specified as the argument
# .join() --> joins the string with an iterable object specified as argument

############
#strings:
#Strings operators:
''' 
+ --> concatenation
* --> repetition and merging
in --> returns true if an element is found in a sequence
not in --> returns true if an element is not found in a sequence
is --> returns true if the two strings are identical
is not --> returns false if the two are identical
'''

#if you try to assign a value to an index in a string you :
#slicing,stepping and selecting:
aRandomSTring = 'lorem ipsum generator testing'
aRandomSTring[::-1] #selects all and steps backward
#string[start:end:step]
aRandomSTring[0::3] #selects every 3 letters

min() #--> minimum alphabetical value of the string
max() #--> opposite to min
len() #--> lenght of string














# a string is a sequence of characters. you can access the characters one at a time with the bracket operator
#a single character can be extraccted as from a vector.
fruit = 'banana'
letter = fruit[1]
letter
#selects the letter in position 1, which corresponds to the second position within the string
letter = fruit[0]
letter
#method to replace characters within a string is with the builtin function
stringresult = fruit.replace('<letter or occurance to replace>','<with what to replace',
                             '<how many times in order, leave empty to replace everythin')
i = 1
fruit[i]
fruit[i+1]
#the index value must be integer

fruit = 'banana'
n = 5.8941616
l = int(n)
fruit[int(n)]

##LEN
# it returns the number of characters in a string

fruit = 'banana'
len(fruit)

# to obtain the last letter on a posiition you must index it with len-1
#string slicing: selecting a range of characters from a string
s = 'monty python'
s[0:5]
s[6:12]
#Returns the parts of the phrase selected in the range
#if you leave the second part of the index free of a number you get the entirety of it
s[5:]
#if you put the same index the return is empty

#strings are immutable, you cannot impose a character within the string content
####### searching function
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index]==letter:
            return index
        index = index + 1
    return 'no value'

find('asdrubalecicciopasticcio', 'u')

######## looping and counting
#counting within the range of a string
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

#STRING ESCAPE CODE:
'\n'#escape code for going on a new line
'\t' #escape code for tabulation
"bingo \" "  #text wrapping, used to go on a new line in the compiler but to keep the text on the same line
'\\' #prints \
'\'' #prints '






###### USEFUL STRING METHODS:




# upper --> takes a string and makes it uppercase.
word = 'banana'
new_word = word.upper()
new_word

phrase = 'cicciopasticcio'
phrase.upper()

#in both cases the return value is the word in uppercase
#in this case the method is called invocation since we are invoking it on the variable
#it has empty paranthesis since it does not take in any rgument

# find --> finds a given letter within a word. returns a value in number
word = 'banana'
index = word.find('a') #it is case sensitive 
index

#if it does not find the given letter it will return a -1.
#it can also find substrings
#it can take a second argument which defines the starting point from which to start searching for a substring

word = 'australopitecus'
index = word.find('lo', 0)
index

word[index]
word[0]


#in any case the index corresponds to the real position of the beginnig of the substring
#where bear in mind that the index 0 is the first index
#we can also set the ending of the searching process.

word.find('te', 3, 15) #15 is the OPTIONAL ARGUMENT
#wherer 15 is the ending char


###### in operator
#the word 'in' is a boolean operator whch takes to strings, and searches for the first string in the second one
#if it appears it will return a true, if it does not it will return a false



'a' in 'banana'

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter) #it prints the letter that is both in one word and in the other.

in_both('antonio','oinotna')


#### String Comparison
#there are three types of relation between strings:
if word == 'banana':
    print('All right, bananas.')

#the word, if equal to banana, will return True.
#there are other ways to compare :

if word < 'banana':
    pass
#the pass statement is used as a marker to complete an incomplete condition




#checks if they are in alphabetical order if they are both lower case,
#if the two words differ in case ( the first is upper and the second is lower ) then we will have a situation
#in which the upper case word comes before the lower case.
#thus remember that before dealing with strings, convert them all to lower or all to upper case
word = word.upper()
word = word.lower()
word


banana.endswith('\n') #to check if the string given ends with a specific character or not, if it does it returns True


#### reading a txt file in python
fin = open('words.txt')
#fin is a common name used to indicate a file object used for input.
#fin.read() #reads everything contained
fin.readline() #reads a line and returns it as a string.
#if you repeat the same command you will read the next line:
fin.readline()
#to get rid of the space and new line at the end just strip it away with the method .strip()

fin = open('words.txt')
line = fin.readline()
word = line.strip() #strips the word of the spaces or of the character selected as arguments
word

fin = open('words.txt')
line = fin.readline()
for line in fin:
    print(line.strip())

#the difference between:
"""
.readline() --> gets as string the line of the document, it changes the cursor on the secondo position

.readlines() --> gets as list of strings all the lines

.read() --> gets as string the total document


"""





#overwriting:
f = open("path", "w") #over
f.write("sequencesstring \n") #\n is necessary in order to tell to write on a new line

#appending:
f =open("path", "a")
f.write("stringtoappend")

#reading:
f = open("path", "r") 

#reading and writing:
f = open("path", "r+" )
or
f = open("path", "w+")

#FILE METHODS:
f.name #returns the name of the file
f.mode #returns the mode we are reading the file
f.closed #returns true if the file has been closed








#searching for a letter 
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True #interesting that the Return True is outside of the cycle cuz we get to the end of the loop

#more generally
def avoids(word,forbidden):
    for letter in word:
        if forbidden in word:
            return False
    return True



#LISTS:
#listed contain elements or items, can be nested and are mutable
#any integer can be used an index
prova = [] #empty list
prova1 = [1,2,3,4,[1,2]] #a nested list
prova2 = [1,2,3,4,5,6,7,8,9] #all numbers from 1 to 9
#the function len works also in lists, as well as the range one.
#to cycle a list:
for i in range(len(prova2)):
    print(prova2[i])
    prova2[i]= prova2[i]*2 #this updates the list and for each value gives a times 2

#to index the last value of a list
#list[-1]
#LIST OPERATIONS:
a = [1,2,3]
b = [4,5,6]
c = a + b #concatenates the list
c = a*3 #gives back an elongated list with the repetition of three times of the list a and they are all concatenated.
a*3 #repeats and increases the list
#LIST SLICES:
a[::2] #i consider each second value starting from the beginning
a[::-1] #i consider each single value going backwards
a[1:3]
a[:3]
a[3:]
c[1:3] = [x,y] #done to update a list in the given elements
#LIST METHODS:
element = 0
a.append(4) #adds an element to the end
a.extend(5,6,7) #dds more than element
a.sort() #arranges the elements of the list from the smallest to the greatest
#DO NOT use a = a.sort() or others, most list.methods are void
a.insert('index','element') #inserts and shifts a given element in a list
a.remove(element) #removes the element from the list
a.pop(index) #pops the element at the index from the list
a.extend(list2) #appends to the list a second list specified as argument
a.index(element) #search for given element and returns the index, only the first occurence
a.sort() #sorts and returns None
a.reverse() #reverses the list
a.clear() #clears the list
a.count(element) #counts the occurances of an element within the list
b = a.copy() #returns a copy of the list







#MAPPING, FILTERING AND REDUCING
lista = [1,2,3,4,5,6,6,7,5,4,3,2,2,3,4]
def add_all(t): #where t is a list
    total = 0 
    for x in t:
        total += x
    return total
#this is a good way , but python is so used to it that there is already an existing function
#that does this:
sum(t) #we REDUCE thus the list

#deleting elements:
t.pop (1) #removes the element at the given index and returns it
del t[1] #removes the element at the given index and does not return it
t.remove(4) #removes the element that corresponds to the argument
#to remove more than one element use the slice:

del t[1:5]

#STRINGS AND LISTS:
#in the print function and in a string we can insert with the special character %d the values of a variable:
inserting = 50
print('the value is: %d' % inserting)

#a string can be considered as an array and it is immutable
#to convert from a string to a list we use the list function
string = 'cicciopasticcio'
t =  list(string) #each character is now separated.

#to split a string into words rather than in characters we use the .split()
#where the .split() argument is the delimeter.
string = 'sono scemo perche lo sono'
t = string.split()

#join works the opposite of split:
t = ['ciccio','pasticcio','sono','scemo']
delimiter = ' ' #a delimiter (which can be empty) is always needed
s = delimiter.join(t)
# all the arguments of the string must be strings

#equal strings are the same objects, equal lists are two different objects if declared separately
def delete_head(t): #taking a list in
    del t[0] #deleting the first object

#when it comes to lists the append returns none while the sum creates a new list
t1 = [1,2,3]
t2 = t1.append(4)
t2 #will return none

#Basically:  a function modifying a lists gives a none, a function creating one will give a list back
#a function modfying must always explicit the return, yet it would still create in that case.



####DICTIONARIES:
.values() #gives a list of values 
.items() #gives the couple of key and value 
#remember to use it
#a dictionary is like a list but more general in which indices are types.
#the collection of indexes is called keys.
#key-value pair are called items
#each key maps to a value
#the function dict() creates a dictionary with no items.

aRandomDict = {}
aRandomDict['gag'] = 'gig' #method to add a new key-value pair to the dictionary.
aRandomDict['gag'] #to retreive the value
print(aRandomDict)

#OPERATORS:
in # --> searhces within the dictionary the presence of a key
del # --> deletes within the dictionary the key-value pair
len #--> returns the number of key-values pairs

#METHODS: 
aRandomDict.get('gag') #--> like using the parenthesis
aRandomDict.pop('gag') #--> removes from the dictionary the key specified and returns the value (which can be stored in another folder)
#if the value is not find with the .pop() the program raises the exception KeyError
aRandomDict.popitem() #--> returns the last item of the dictionary (as a tuple of key,value)
.items() #--> creates an object consisting in a list of tuples, each one with two elements
.keys() #--> creates a dict_keys object consisting in a list in which each element is one key
.values() #--> creates a dict_values object consisting in a list in which each element is one of the value of the dictionary
.update(dict2) #--> appends the key-value pair of the new dict to the first specified
.clear() # --> self explanatory






#FUNCTIONS:
len() #lenght of the keys of the dict
dict() #creates an empty dictionary
max() #returns the maximum value of the keys (keys only)
min() #returns the opposite
sorted() #returns the list of the keys in an ascendent order








eng2sp = dict()
eng2sp = {
    'one' : 'uno',
    'two' : 'dos',
    'three' : 'tres'
}
#the order of the dictionary is not predictable , but that is not a problem since they are not indexed with integers
#to extract a specific value we select a key - index:
eng2sp['two']

#if the key is not in the dictionary you will get an exception --> KeyError: ...
#Len() gives the number of key-value pairs
len(eng2sp)
#In function appears too and tells you if there is such a key in the dictionary
'one' in eng2sp #will return true
#does not work with the values

#to work with values we use
#Values()

'uno' in eng2sp.values()

#Lists using in will take proportionally much time to their lenght, dictiory not since they have hashtables.
#summing up to dictionaries  --> statistical application (page 200)

#you can iterate throught a dictionary:
anexampleofdict = {'key1':1,'key2':2}
for key,value in anexampleofdict.items():
    print(key,value)
    

#TRAVERSING DICTIONARIES:
#keys are traversed with the use of for loop:
for key in anexampleofdict:
    continue

#we can also traverse key-value pairs using the for loop with .items():
anexampleofdict = {'key1':1,'key2':2}
for key,value in anexampleofdict.items():
    print(key,value)


#Looping dictionaries:
dictionary = {}
def print_dict(h): #dictionary --> h
    for c in h:
        print(c, h[c])

#to sort out the dictionary we use the the sorted() function
print(sorted(dictionary))

#REVERSE LOOKUP:
def reverse_lookup(d,v): #takes in a value and a dictionary d.
    for k in d:
        if d[k] == v:
            return k
    raise LookupError

#this function  will return the index of the dictionary if it meets the value inputted
#and RAISES a built in exception in the case in which it does not find that given value
#RAISE statement causes an exeption.
#return always gets out of the function
#a reverse look up is slow, try to use the forward (coming from the index)

#Dictionaries and LISTS:
#lists can appear as values in a dictionary, for example if you are given a dictionary with certain keys and multiple values, for each value you
#will have multiple keys, there is a way to invert them:

def invert_dict(d):
    inverse = dict() #declare new dictionary
    for key in d:
        val = d[key]
        if val not in inverse: #where val is the key in the inverse
            inverse[val] = [key] #in the index val add key in the case val is not a key in inverse
        else:
            inverse[val].append(key) #to the index val lists append the key to addup to the list

#storing previously calculated results in a dictionary simplifies the work 
#global variables - established in the __main__
#if you reassign in a function the global variable it will die within the function and keep its value outside
#the most popular use of global vars is the flag variables containing boolean chars

been_called = False #is a global statement
#and to recall a global statement within a function we declare it
count = 3
def counting():
    global count
    count +=1 #and this will modify the global count since i declared --> i make it mutable if i recall it in
    count

counting()

#if i have variable which de facto is mutable also in global, i dont need to recall it.
dictionary = {0:0 , 1:1 , 2:2}

def example3():
    dictionary[2] = 1 #it will change the value in key 2 with 1.
    dictionary[3] = 1 #it will add a 1 as key 3.

#BUT if you want to reassing the dictionary you have to recall and declare it as global within the function.

####TUPLES -- IMMUTABLE sequence of values, indexed by integers
##TUPLE FUNCTIONs:
len() #--> returns lenght of the tuple
tuple() #--> declares the tuple or converts an iterable to it
max() #--> returns the element with the highest number or the string with the initial letter having the highest alph. value
min() #same but opposite
#the max() and min() have to have the same type of objects within, a tuple with  both a string and a number wont work
sorted() #returns a new list with ascendent order
sum() #SUMS  all elements of the tuple

#METHODS
t = ()
t.index(element)
t.count(element)






t = ('a', 'b', 'c', 'd') #parenthesis are not explicitely needed, but it is much better to enclose them
#to create an empty tuple:
t = tuple()
#to create a tuple in which each element is a part of it just type a string and force it considered to be a tuple
t = tuple('lupino')
t #it will return each character separately
#slices select the indexed elements but you cannot modify em
#yet you can replace a tuple and change referrence:
t = ('A') + t[1:]
t #will return t but with the A in the front as first element

#COMPARISON OF TUPLES:
(0,1,2) < (0,3,4) #will return TRUE
(0, 1, 2000000) < (0, 3, 4) #will return TRUE
# Python starts by comparing
#the first element from each sequence. If they are equal, it goes on to the next elements, and
#so on, until it finds elements that differ. Subsequent elements are not considered (even if
#they are really big).

###TUPLE ASSIGMENT:
#to swap a and b
#INSTEAD OF:
temp = a
a = b
b = temp
#we do
a, b = b, a

#IN GENERAL -- the left side can be anything:
email = 'apuzalkov@gmail.com'
username, domain = email.split('@')
#it will return username as apuzlakov and domain as gmail.com

###TUPLES AS RETURN VALUES:
#divmod(x,y ) where x/y and returns a tuple with the values of the quotient and the remainder
t = divmod(7,3)
t #returns a tuple of 7/3 --> (2,1)
quot, rem = divmod(7,3) #the elements on the left must have a logical correlation with the elements on the right
quot #2
rem  #1

#to pass a tuple or to pass multiple variables as a tuple in the function we precede the parameter declared with '*'
#gathering
def printall(*args): #takes in all the values and prints them as a tuple (GATHERING)
    print(args)

#scattering
t = (7, 3)
divmod(*t) #in this way takes the tuple, which is a single element, scatters it and can get the two arguments

def sumall(*args): #gets an indefinite number of numbers
    sumtot = sum(args)
    return sumtot

sumall(1,2,3,4,6,7,7,8,4,6,2,23,5,5,6,6)


#ZIPPER: takes a string and a list and returns tuples iteracted.
s = 'abc'
l = [0,1,2]
zip(s, l)
for pair in zip(s,t):
    print(pair)

#Dictionaries and tuples:
#there is a method called .items() which returns for each pair of keys and values the tuple corresponding
for key, value in d.items():
    print 
d = {
    'a':'1',
    'b':'2',
    'c':3,
    }

t= d.items()

for key,value in d.items(): 
    print(key,value)

#the combination of dict and zip can create a new dictionary.
t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)

#OR

d = dict(zip('abc', range(3)))
directory[last, first] = number
#The expression in brackets is a tuple. We could use tuple assignment to traverse this
#dictionary:
for last, first in directory:
    print(first, last, directory[last,first])
#This loop traverses the keys in directory, which are tuples. It assigns the elements of each tuple to last and first, then prints the name and corresponding telephone number.



# creating an empty non typed variable:
z = None







###### GUI - THEORY:
import tkinter as tk


#to create a new window
window = tk.Tk()
#to add a widget
#greeting = tk.Label(text='hello world')
#greeting.pack()
#with window.mainloop() python listens for events
#window.mainloop() #where mainloop is the method for listening to new events
#the following are all types of widgets
#label
#button
#entry
#text
#frame

#Useful label:
label = tk.Label(
    text='Label_txt',
    fg="blue", #can be hexadecimal
    bg='green', #can be hexadecimal
    width=50,
)

#getting user imput
#.get() , .delete() it deletes the text, .insert() inserts the text
entry = tk.Entry(
fg = 'yellow',
bg= 'blue',
width = 50

)
#entry get a oneline user input

entry.pack()
name = entry.get()
window.mainloop()
name

#useful button
button = tk.Button(
    text='Click me',
    fg='white',
    bg='blue'

)

""" --> this GUI tutorial is just an introduction and reminder, the rest will be moved to a new PY file""" """Maybe"""











#######TYPE OF ERRORS:
#aminly the following:
#syntax errors --> error in the writing of the code (syntax)
#runtime error --> error in the code   - ex: a non declared variable
#semantic erros: --> the program runs and executes but the result is not the expected one




"""
AssertionError: Raised when the assert statement fails.
AttributeError: Raised on the attribute assignment or reference fails.
EOFError: Raised when the input() function hits the end-of-file condition.
FloatingPointError: Raised when a floating point operation fails.
GeneratorExit: Raised when a generator's close() method is called.
ImportError: Raised when the imported module is not found.
IndexError: Raised when the index of a sequence is out of range.
KeyError: Raised when a key is not found in a dictionary.
KeyboardInterrupt: Raised when the user hits the interrupt key (Ctrl+c or delete).
MemoryError: Raised when an operation runs out of memory.
NameError: Raised when a variable is not found in the local or global scope.
NotImplementedError: Raised by abstract methods.
OSError: Raised when a system operation causes a system-related error.
OverflowError: Raised when the result of an arithmetic operation is too large to be represented.
ReferenceError: Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError: Raised when an error does not fall under any other category.
StopIteration: Raised by the next() function to indicate that there is no further item to be returned by the iterator.
SyntaxError: Raised by the parser when a syntax error is encountered.
IndentationError: Raised when there is an incorrect indentation.
TabError: Raised when the indentation consists of inconsistent tabs and spaces.
SystemError: Raised when the interpreter detects internal error.
SystemExit: Raised by the sys.exit() function.
TypeError: Raised when a function or operation is applied to an object of an incorrect type. <-- also this one is very frequent
UnboundLocalError: Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError: Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError: Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError: Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError: Raised when a Unicode-related error occurs during translation.
ValueError: Raised when a function gets an argument of correct type but improper value. <-- one of the most frequent
ZeroDivisionError: Raised when the second operand of a division or module operation is zero.
"""
#EXCEPTION handling:
import tkinter as tk
#to handle this kind of errors we can use the try and expect 
try:
    num = int(input('insert a numerator: '))
    den = int(input('insert the denominator: '))
    print(num/den)
except:
    print('stop doing mistakes you silly')
    input('press a button you silly...')
    print('being silly is not an excuse')
    print('it is "making mistakes" and not "doing mistakes"')
    finestra = tk.Tk()
    label = tk.Label(
        text='you are a silly'
    )    
    label.pack()
    finestra.mainloop()

#we can be more specific with the type of error exception:
try:
    z = int(input(''))
except ValueError:
    print('something')
except NameError: #we can specify particular errors in fact
    print('something else')
except:
    print('all other errors')
    
    
    
    
  
#the main difference between strings, tuples, lists and dictionaries:
#strings: immutable and contain only text
#tuples: immutable and contain any value
#list: mutable and indexed orderly with integers
#dictionaries: mutable and indexed with keys

#in lists we can also contain tuples
anExample = ['list',1,3,(1,2,3),5]
#and if iter through it we can see that the tuple is within 

var = iter(anExample)
print(next(var))
print(next(var))
print(next(var))
print(next(var)) #e questa ?? la tupla
    



######WEBBROWSER
import webbrowser
webbrowser.open("url")



######FILENAMES & PATHS:
import os #a useful library to interact with the local paths.

os.listdir('path')
#gives the list of files

os.path.join(path,filename)
#returns the path and filename of the given filename

os.path.isifle(path)
#returns true if the path is referring to a file, false otherwise


#RANDOM MODULE:
import random
random.random() 
#returns a random decimal number between 0 and 1

random.randint(min,max)
#returns a random integer number between min and max, both endpoints INCLUDED

random.choice(list)
#returns a ranodm element from the list given as argument

random.randrange(min,max,step)
#returns a random integer between min and max with an increace of step






#######Pypi is the official site for modules

###openpyxl



###ripassare:
#ranges
#vedere errori simulazione
#imparare classi




#########CLASSES:
#class is the blueprint
#object is the concrete INSTANCE of the class
#methods are actions that the object can do
#object: : is the abstract definition used for elements that are characterized by 
        #attributes (how it is made) and methods (how we can modify and use it)
#Class:: is the abstract description of an object. It represents the set of objects 
        #(??family??) of a certain type. A class is made of attributes and methods 
#instance: is the term used for a specific ??real?? object of a class
#BUILDING A CLASS:
class Name(): #definition and name
    """[summary]
        tutorial
    Returns:
        [type]: [description]
    """ #docstring description
    def __init__(self,first,second,third = 88): #constructur method where all the attributes are specified
        #attribute #it includes calls for funtions as well as opening of files and access to db
        #attribute
        #attribute
        self.first = first
        self.second = second
        self.third = third
        self.another = 0 #initilzied and later can be recalled in the object and can be assigned a value
        
    def method(self): #method --> instruction, self --> positional requirement
        #instruction
        #instruction
        #instruction
            pass
        
    #special method
    def __str__(self):
        #used to create a printout of the class when called
        t = 'This is a class example' + self.third            
        return t #must always end with the return statement
                
    

instance = Name(1,2,3)
instance.another = 6
Name.method() #you can have specific parameters for the  method
#but at least when the declared you need to have the self parameter
print(instance) #will print the object __Str__


#to find the classes of libraries you can use the following function:
import requests
dir(requests) #checks the library directory
class coin():
    def __init__(self):
        self.fixedvalue = 0
        self.startface = 'Head'
        self.resultOftoss = self.startface
    
    def toss(self):
        import random as R
        if R.randint(1,2) == 1:
            self.resultOftoss = 'Head'
        else:
            self.resultOftoss = 'Tail'
        print('toss result is: ', self.resultOftoss)
        return self.resultOftoss
    
"""to create a class we declear it with the keyword class"""
class test_class:
    x = 10
#objects are now derived from the class we created
p1 = test_class() #THis creates the object p1
print(p1.x) #this calls the value of x within the class itself

#the __init__() function
"""it used to assigned the values within the class
to be later recalled by the object"""

class test2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p1 = test2('John', 36)  #creates the object and provides with the variables init
print(p1.name) #recalls the object and the variable name 
print(p1.age) #recalls the object and the variable age.
#the __init__() function is called each time the class is called to create the object.

##OBJECT METHDOS: objects can also contain methods --> functions belong to the object
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def functest(self):
        print('hello my name is ' + self.name)
        
obj1 = Person('John', 36)
obj1.functest() #this recalls the function within the object which uses the data provided with the init

#we can modify object properties:
p1.age = 40 #this will change the age in the object (the class is unchanged)
#as well as you can delete obj properties
del p1.age
#or delete the object itself
del p1
#the pass statement is used to fill an otherwise empty class

class pippo:
    pass

##PYTHON INHERITANCE:
"""inheritance allows us to deine a class that inherits the properties of the other classes"""
"parent class" # is the class being inherited from, also called base class
"child class" # is the lcass that inherits from another class also called derived class

#the parent class is declared as a normal class:
class parent:
    def __init__(self, fname,lname): #gets the parameters of the object
        self.firstname = fname
        self.lastname = lname

    def printnames(self):
        """a function which gives back printed the fname and lname concatenated"""
        print(self.firstname, self.lastname)
        
x = parent('antonio','puzalkov')
x.printname()






#HIERARCHIES AND INHERITANCE:
''' 
parent class(superclass)
child class (subclass):
- the child class inherits all the data and the methods of the parent class
- adds more info and methods
- overwrites methods
the following is an example:
'''

class student(Person): #class parent specified as 
    def __init__(self, IDnum, name,age): #args from the parent are still included since they have to be insert
        Person.__init__(self,name,age)  #__init__ method from the parent class recalled to be filled by user/programmer
        self.idnum = IDnum #new variable added for the child class
        
    def __str__(self):
        return super().__str__() #will reutnr the __str__ of the parent
    #YOU CANNOT HAVE BOTH - JUST FOR EXAMPLE
    def __str__(self):
        t = 'a new string for explanation ' #will return this str
        return t   #redefined method
    
    def method(self):
        #a new method, original for the child
    
    #all other methods from the father/parent class are preserved
    #and they can be called with an instance specified with class child
    
    





class child(parent):
    pass
#you cna also add other things to the child class and still inherit the parent
#if you dont want to add anything else we just put the pass method at the end

#we can add the __init__() function to the student class:
class student(parent):
    """[summary]
    once i have generated a given docstring, it can be printed uising the help() function in the python console
    
    Args:
        parent ([type]): [description]
    """    
    def __init__(self, fname, lname):
        #add anything in it
    #if we add the __init__() function in the child the parents' one will be overwritten.
    
    #to keep the __init__ function of the parent we have to add a call of it:
        parent.__init__(self,fname,lname)
        #or we can inherit the parameters without indicating the name of the parent
        super().__init__(fname,lname)

help(student)














###USEFUL SHORTCUTS:
"""
ctrl+shift+L --> selects all occurences of that word.

(ctrl+K) + (ctrl+C) --> turns all the selected lines into a comment
"""

#for the exam:
"""
rember the " rather than the '
rembember the return statement
be formal
"""



