def most_frequent(string): #takes in the string to be evaluated
    letters = {}
    for x in string: #here x is a counter, but does not have integer value.
        letters[x] = letters.get(x, 0) + 1

    return letters


ciccionis = 'guadete gaudete christiusi oest natus, ex maria, virgine, gaudete'
most_frequent(ciccionis)        
 

 