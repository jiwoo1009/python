from turtle import *
from random import *
bgcolor('khaki')
color_list=['cyan','magenta','green','gold','blue','wheat1','tan1','salmon2']

def draw_figure(angle):
    distance=1
    for a in range(100):
        fd(distance)
        right(angle)
        distance= distance+2

speed(0)
loop='y'

while loop=='y':
    angle=input('터틀이 회전할 각도 입력')
    color(choice(color_list))
    draw_figure(int(angle))
    loop=input('계속하려면 y, 멈추려면 n을 일력')
    if loop=='n':
        break
    else:
        up()
        x=randint(-300,300)
        y=randint(-300,300)
        goto(x,y)
        down()
