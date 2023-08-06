import random

n= random.randint(1,100)


while True:
    x= input("뭘까요? ")
    g=int(x)
    if g==n:
        print("정답")
        break
    if g < n:
        print("너무 작아요.")
    if g > n:
        print("너무 커요.")
