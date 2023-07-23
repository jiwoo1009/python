import turtle as t
t.shape("turtle")
t.speed(0)
radius=input("반지름")
radius=int(radius)
x=0
y=0
for a in range(3):
    t.goto(x,y)
    t.down
    t.circle(radius)
    radius=radius+20
    x=x+100
