def sum_digits():
    x = 0
    thedigit = str(input("enter a number: "))
    for i in thedigit:
        x += int(i)
           
    return x

sum_digits()
        