import turtle as t
t.speed(0)
a=int(t.numinput('원 그리기','장미에 몇 개의 원을 그리기 원하세요?', 6))
for k in range(a):
    t.circle(100)
    t.left(360/a)
