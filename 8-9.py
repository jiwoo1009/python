import turtle as t
t.speed(0)
for x in range(100):
    t.fd(x)
    if x %2==1:
        t.left(110)
    else:
        t.rt(150)
    
    
