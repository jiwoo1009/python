import random
number = random.randint(1,30)
guess = int( input("1부터 30사이의 숫자를 맞춰보세요 :") )
counter=0
while guess != number:
    counter= counter + 1
    if guess > number:
        print("너무 높습니다. 다시 시도 해주세요.")
    if guess < number:
        print("너무 낮습니다. 다시 시도 해주세요")
    guess = int( input("1부터 30사이의 숫자를 맞춰보세요 :") )
print(guess,"맞습니다! 당신이 이겼습니다!", counter, '번만에 맞추었군요')
    
