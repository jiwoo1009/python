import turtle as t
import random
t.shape("turtle")

geobuk=t.Turtle( )#거북이 복제본 만들기
geobuk.shape('turtle')
geobuk.color('blue')
geobuk.speed(0)

t.shape("turtle")
t.color('red')
t.speed(0)
t.shapesize(2,2,3)

for a in range(500):
    t.setheading(random.randint(1,360) )#방향보기
    t.fd(10)
    geobuk.left(random.randint(1,360) )
    geobuk.fd(15)
