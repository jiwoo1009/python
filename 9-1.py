import random
for x in range(5):
    a=random.randint(1,20)
    b=random.randint(1,20)
    dab=a+b
    c=str(a)+"+"+str(b)
    d=input(c)
    d=int(d)
    if d== a+b:
        print('정답')
    else:
        print('오답')
        
     
     
