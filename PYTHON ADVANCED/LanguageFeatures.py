#all imports must be at the top
#each line should be limitd to 79 characters
#indents should hav eithere a tab or 4 spaces


##WHISPACE CONVENTIONS:
"""do not use space with parenthesys
two blank rows to distance each function in a class"""


##WHAT IS CONSIDERED FALSE:
"""
False and None are false
numeric 0 is false
decimal(0) or fraction(0,x) are false
empty sequences such as tuples, strings and dict are false
if i impose bool() on these items i will get out False 

we use the operators:
and
or
not
we all know what they stand for


"""


##STRINGS vs BYTES:
"""bytes are not the same as strings
you have to decode bytes specifically to strings
for example:
"""
s = 'a random string'
b2 = s.encode('utf-8')
print('b2')
s2 = b2.decode() #and we can use different type of encoding, such as utf-32
print(s2) 


##TEMPLATE STRINGS:
from string import Template
templ = Template("something -  ${title} by ${author}")
str1 = templ.substitute(title ='the title of it',author = 'antonio' )
print(str1)
#suppose now i want to use to select and pass the dictionary to substitute in the string
data = {
    "author" : "Antonio Puzalkov",
    "title" : "Advanced Python"
}
str3 = templ.substitute(data)
print(str3) #this method of substitution is very good since it gives you the ability to do substitute data and print templ strign without the need to manage directly the data itself



