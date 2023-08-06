import turtle as t
import random
t.shape("turtle")
for a in range(100):
    q=-t.window_width( )//2
    w=t.window_width( )//2
    x=random.randint(q,)
    y=random.randint(-t.window_height( )//2,t.window_height( )//2)
    t.goto(x,y)
