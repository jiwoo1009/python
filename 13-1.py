import turtle as t
def right( ):
    t.seth(0)#방향보기
    t.fd(20)
def up( ):
    t.seth(90)
    t.fd(10)
def left( ):
    t.seth(180)
    t.fd(10)
def down( ):
    t.seth(270)
    t.fd(10)
def clear( ):
    t.clear( )
t.shape("turtle")
t.speed(0)
t.onkeypress(right,"Right")
t.onkeypress(up,"Up")
t.onkeypress(left,"Left")
t.onkeypress(down,"Down")
t.onkeypress(clear,"Escape")
t.listen( )
