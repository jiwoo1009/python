import turtle as t


    t.up( )
    t.fd(x,y)
    t.down( )
    t.fillcolor(C)
    angle = 360.0 /sides
    t.begin_fill()
    for u in range(sides):
        t.fd(length)
        t.left(angle)
    t.end_fill()
for g in range(10):
    color = random.choice(['white','yellow','blue','skyblue','orange','green'])
