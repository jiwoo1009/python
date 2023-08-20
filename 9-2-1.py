import turtle as t
import random
t.bgcolor('black')
colors =['blue','green','magenta','red']
for a in range(100):
    t.speed(9999999999)
    t.color( colors[a % 4] )
    x=random.randint(-t.window_width( )//2, t.window_width( )//2)
    y=random.randint(-t.window_height( )//2,t.window_height( )//2)
    t.up()
    t.goto(x,y)
    t.down()
    num=random.randint(5,40)
    for k in range( num):
        t.fd(k)
        t.left(92)
