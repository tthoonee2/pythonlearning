"""Prerequisites:
Visual code.

We start with the exercise set of ‘fileinput’.
First thing is file handling
"""
f = open('inputFile.txt', 'r')
print(f.read())
f.close()
#rhis will open and print the entire file

count = 0
f = open('inputFile.txt', 'r')
for lin in f:
    print(str(count)+lin)
    count+1
f.close()

#i know want to check if the person passed

f = open('inputFile.txt', 'r')
for lin in f:
    line_split = lin.split() #splitting based on the space
    if line_split[2] == 'P':   #checking wheter the third element of the list of the split is a P (passing)
        print(lin)
f.close()


#know we want to write our findings to another file
f = open('inputFile.txt', 'r')
passfile = open('passfile.txt','w') #this opens a new file and writes in it
failfile = open('failedfile.txt', 'w')
for lin in f:
    line_split = lin.split()
    if line_split[2] == 'P':
        passfile.write(lin)
    else:
        failfile.write(lin)

f.close()
passfile.close()


