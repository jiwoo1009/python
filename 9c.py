import random
a=random.randint(1,30)
b=random.randint(1,30)
print(a, "+", b, "=")
c=input("?")
c=int(c)
if c==a+b:
    print('정답')
else:
    print('틀림')
