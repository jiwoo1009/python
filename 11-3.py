import random
import turtle as t
c=['cyan','magenta','green','gold','blue','wheat1','tan1','salmon2']
t.speed(0)
def draw(n):
    for a in range(n):
        x=random.randint(-t.window_width()//2,t.window_width()//2)
        y=random.randint(-t.window_height()//2,t.window_height()//2)
        radius=random.randint(10,100)
        t.up( )
        t.goto(x,y)
        t.color(random.choice(c))
        t.down( )
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
n=int(input("원의 개수는?"))
draw(n)

