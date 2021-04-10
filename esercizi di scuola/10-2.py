x = int(input('insert the first number: '))
y = int(input('insert the second number: '))
add = x+y
div = x/y
mult = x*y
sub = x-y
floor = x//y
rem = x%y
print("addition:",' '* (20-len('addition')),add)
print("division:",' '* (20-len('division')),div)
print("multiplication:",' '* (20-len('multiplication')),mult)
print("subtraction:",' '* (20-len('subtraction')), sub )
print("floor division:",' '* (20-len('floor division')),floor)
print("division remainder:",' '* (20-len('division remainder')),rem)
