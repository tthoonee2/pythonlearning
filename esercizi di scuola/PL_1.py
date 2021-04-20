import turtle as t
import math

cat1 = int(input('input the first cat: '))
cat2 = int(input('input the second cat: '))

def pythagoras(c1,c2):
    hypo = math.sqrt(c1**2 + c2**2)
    return hypo

def drawhypo():
    hyp = pythagoras(cat1,cat2)
    t.forward(cat1)
    t.left(90)
    t.forward(cat2)
    t.left(math.asin(cat1/hyp))
    t.forward(hyp)
    
drawhypo()
    
    


#Harmonic sum
def harmonic_sum(N, a):
    result = 0
    for n in range(1, N+1):  #range is needed whenever the variable is not iterable
        element = 1 / n**a   #N+1 and starting from 1 (1, N+1)
        result += element

    return result
#CAN WE OPTIMIZE THIS FUNCTION. --> 


def roll_dice(win_num, n_rolls = 1):
    score = 0
    import random
    for i in range(n_rolls):
        dice1 = random.randrange(1,6,1)
        dice2 = random.randrange(1,6,1)
        dice3 = random.randrange(1,6,1)
        if win_num == dice1 == dice2 == dice3 :
            score += 1
            
    return score
        
    

