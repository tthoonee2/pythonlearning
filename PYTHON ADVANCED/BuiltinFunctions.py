#link to python built in functions::
url = "https://docs.python.org/3/library/functions.html" #very useful

##THE MAIN BUILTIN FUNCTIONS:
#any
listing = [1,2,3,4,5,6,0]
any(listing)
#this function outputs a True if it finds any value which would give the true value ( the only value which in this case could give us a False is the 0)

#all
all(listing)
#his function outputs a True if all the values give a True valus, since there is a 0 we get a False.

#min & max
print('min: ',min(listing))
print('max: ',max(listing))
#gives either the max or min value of a given list

#sum
print('sum: ',sum(listing))
#gives the sum of the values of the list




#ITERATORS:
#we define a couple of lists to iterate into
days = ['sun','mon','tue','wed','thu','fri','sat']
giorni = ['lun','mart','merc','giov','ven','sab','dom']
#use iter to create an iterator over a colleciton
i = iter(days) #once ive done it i cann access the next object with the next object 
print(next(i))
print(next(i))
print(next(i))

#i can usee it a s function and a sentinel   #END OF FILE - #SEARCHING FOR SENTINEL
fp = open('file.txt', 'r')
for line in iter(fp.readline, ''): #this code iterates through all the lines upuntil it finds an empty one , thus the end of the file
    print(line)
       
#enumerate: provides also a counter not only the value
for i,m in enumerate(days, start = 1): #enumerate takes the values i,m where i is the index and m the value and it gives back and cycle through the list as if it was another list
    print(i,m)
    
#zip: use it to combine sequences
for m in zip(days, giorni):
    print(m) # i get a tuple called m with the two lang-days
    
#combination of zip and enumerate
for i,m in enumerate(zip(days,giorni),start = 1): #if the two sequences are not long enough, the cycle terminates at the shortest list
    print(i, m[0], '=', m[1], ' in italian')   #we use m[0] and m[1] since m is a tuple and we consider the first value and the second



#Use transform functions like sorted, filter, map
##FILTER FUNCTION:
alllist = (1,2,3,4,5,6,7,8,9)

def filterfunc(x):
        if x % 2 == 0:
            return False
        return True

onlyodd_list = list(filter(filterfunc,alllist)) #the filter removes all the false values.
#it iterates throught the list and uses the function to determin whether the value at that moment is
#meant to be True or False




#you could the same with lower and uppercase

def squarefun(x):
    return x**2

square  = list(map(squarefun, alllist))
print(square)
###MAP iterates and applies a function on the values.

###SORT






