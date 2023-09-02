import turtle as t
a=t.Turtle()
a.color('red')
a.goto(0,200)
a.speed(0)
run=True
def track():
    global run
    angle=a.towards(t.pos())
    a.seth(angle)
    a.fd(10)
    if run:
        t.ontimer(track,100)
    if t.distance(a)<10:
        run=False
        t.write('Game Over',False,'center',('Arial',50))
        t.hideturtle()
        a.hideturtle()
def up():
    t.seth(90)
    t.fd(10)
def down():
    t.seth(270)
    t.fd(10)
def left():
    t.seth(180)
    t.fd(10)
def right():
    t.seth(0)
    t.fd(10)
t.onkeypress(up,"Up")
t.onkeypress(down,"Down")
t.onkeypress(left,"Left")
t.onkeypress(right,"Right")

t.listen()
track()
