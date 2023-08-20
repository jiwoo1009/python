import random
country=['영국','프랑스','독일','오스트리아','스페인','포르투갈','이탈리아']
capital=['런던','파리','베를린','비엔나','마드리드','리스본','로마']
for k in range(1,6):
    a=random.randint(0,len(country)-1)#0
    b=country[a]+"수도는?"#영국의 수도는?
    print(b)
    c=input("?")
    if c==capital[a]:
        print('오~ 대단한데~')
    else:
        print('응..아니야...')
    
