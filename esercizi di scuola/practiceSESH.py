#pythagoras
import math
def pythagoras(cat1,cat2):
    hypo = math.sqrt(cat1**2 + cat2**2)
    return hypo

def show_hypo():
    cat1 = float(input('enter cat1: '))
    cat2 = float(input('enter cat2: '))
    print(pythagoras(cat1,cat2))
    print(math.floor(pythagoras(cat1,cat2)))
    print(math.ceil(pythagoras(cat1,cat2)))
    
show_hypo()
    
    
#sum
import math
def harmonic_sum(N, a):
    result = 0
    for n in range(1,N):
        result += 1/(n**a)
    return result

x = harmonic_sum(1000, 5)
    
    
#roll the dice
def roll(win,n_rolls):
    import random
    result = 0
    dice1 = 0
    dice2 = 0
    dice3 = 0
    for n in range(n_rolls):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
        if dice1 == dice2 == dice3:
            result += 1
    return result

roll(5,10000)