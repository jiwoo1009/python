import random
import turtle as t
t.shape("turtle")

def square(length):
    for a in range(4):
        t.fd(100)
        t.left(360/4)
def drawit(x,y):
    t.up( )
    t.goto(x,y)
    t.down( )
    t.begin_fill()
    t.color(random.choice(["blue","red","yellow","green","gray","purple","orange"]) )
    square(random.randint(30,100))
    t.end_fill()

t.onscreenclick(drawit)
