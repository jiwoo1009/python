import turtle as t, random
d=0
def jump():
    global d
    while t.ycor()>0:
        t.fd(15)
        t.rt(5)
    t.dot(20,'blue')
    d=t.distance(-200,10)
    t.sety(random.randint(50,300))
    d=[d,t.xcor()]
    t.write(d,True,'center',('Arial',15))
    t.goto(-200,10)
def up():
    t.left(2)
def down():
    t.right(2)
t.goto(-300,0)
t.goto(300,0)
t.up()
t.goto(-200,10)
t.onkeypress(jump,'space')
t.onkeypress(up,'Up')
t.onkeypress(down,'Down')
t.listen()
