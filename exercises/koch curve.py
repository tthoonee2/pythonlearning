import turtle
koch = turtle.Turtle()


#def draw(t, length, n):
#   if n == 0:
#       return
#   angle = 50
#   t.fd(length*n)
#   t.lt(angle)
#   draw(t, length, n-1)
#   t.rt(2*angle)
#   draw(t, length, n-1)
#   t.lt(angle)
#   t.bk(length*n)


def draw2(t, lenght):
    if lenght < 3:
            t.fd(1)
            t.lt(60)
            t.fd(1)
            t.rt(120)
            t.fd(1)
            t.lt(60)
    else:
        for i in range (10):
            t.fd(lenght/3)
            t.lt(60)
            t.fd(lenght/3)
            t.rt(120)
            t.fd(lenght/3)
            t.lt(60)

draw2(koch, 30)




