import turtle as t
import random
t.speed(0)
factory=[]
c=["blue","pink","red","magenta","cyan"]
for n in range(100):
    factory.append(t.Turtle ()    )
    factory[n].color(c[n%5])
    x=random.randint(-t.window_width()//2, t.window_width()//2)
    y=random.randint(-t.window_height()//2,t.window_height()//2)
    factory[n].speed(0)
    factory[n].goto(x,y)
    
