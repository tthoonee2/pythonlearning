import turtle
import math

bob = turtle.Turtle()

def polygon(t,n,lenght):
    angle = 360/n
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)

def circle(t,r):
    circumference=2*math.pi*r
    n=50
    lenght = circumference
    polygon(t,n,lenght) #i can recall the polygon function inside this function with other parameters

circle(bob, 30)