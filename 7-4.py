import turtle as t
t.shape("turtle")
t.speed(0)
radius=input("반지름")
radius=int(radius)
color=input("원의 색깔을 입력하시오: ")
t.color(color)
t.begin_fill( )
t.circle(radius)
t.end_fill( )
