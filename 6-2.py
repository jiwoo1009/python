import turtle as t
t.bgcolor('black')
colors=["purple","orange red","magenta","gold"]
t.speed(0)
for x in range(200):
    t.color(colors[x%4])
    t.fd(x)
    t.left(360/8+2)

