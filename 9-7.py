import turtle as t
import random
t.shape("turtle")
for a in range(10):
    t.speed(0)
    s=random.randint(10,200)
    t.circle(s)
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    r=random.random( )
    g=random.random( )
    b=random.random( )
    t.color(r,g,b)
    t.up( )
    t.goto(x,y)
    t.down( )
    
