import turtle
koch = turtle.Turtle()


def draw(t, lenght):
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

draw(koch, 30)




