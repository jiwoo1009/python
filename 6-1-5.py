import turtle as t
colors["purple","orange red","magenta","gold"]
t.speed(0)
for x in range(200):
    t.circle(x)
    t.rt(360/4+2)
    t.color(color[x%4])
