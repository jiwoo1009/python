import turtle as t
t.bgcolor('black')
colors=["purple","orage red", "magenta" , "gold"]
t.speed(0)
for x in range(200):
    t.color(colors[x%4])
    t.circle(50)
    t.left(92)
