import time
phrase = 'scemolone '

def do_twice(f, x):
    f(x)
    f(x)

def print_spam(y):
    print(y)

#do_twice(print_spam , phrase)

def do_four(double_function,printing , phrase):
    double_function(printing, phrase)
    double_function(printing, phrase)


do_four(do_twice, print_spam, phrase)
