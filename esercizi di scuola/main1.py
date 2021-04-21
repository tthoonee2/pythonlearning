def even_numbers(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    if num1 > num2:
        for i in range(num2,num1):
            if i % 2 == 0:
                print(i)
            else:
                pass
    elif num1<num2:
        for i in range(num1,num2+1): #always add it to the end the +1 since it will iterate otherwise going up to the second number
            if i % 2 == 0:          
                print(i)
            else:
                pass

#for the compiler it is much better to write the function within the editor rather
#due to lag and glitch
