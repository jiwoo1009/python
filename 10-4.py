import random
while True:
    num=random.randint(0,9)
    print(num)
    if num != 4:
        continue
    else:
        break
print('프로그램이 종료되었습니다')
