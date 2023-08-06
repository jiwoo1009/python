import random
nickname=['뱀','사자','상어','호랑이','독수리']
for x in range(5):
    input('엔터키를 누르면 당신의 별명 보기...')
    y_nickname=random.choice(nickname)
    print('당신의 별명은...',y_nickname)
    order=nickname.index(y_nickname)
    print(y_nickname,'는 리스트에서',order,'번째 있군요..')
