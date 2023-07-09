import turtle as t
color=["red","blue","yellow"]
t.speed(0)
for a in range(3):
    t.color(color[a])
    t.begin_fill( )
    for x in range(6):
        t.fd(100)
        t.left(360/6)
    t.end_fill( )
    t.left(360/3)
