height= input('키를 입력해주세요')
height=float(height)*0.01
weight=input('체중을 입력하세요')
weight=float(weight)
bmi=weight/pow(height,2)
print('BMI 값은', bmi)
if bmi<18.5:
    print('말랐어요 더 먹어요 ')
elif bmi  <25:
    ('표준체형 입니다. ')
elif bmi <30:
    print('비만이에요.운동하세요')
else:
    print('고도 비만이에요! 그만 드세요...')
