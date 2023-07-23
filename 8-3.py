country=['브라질','미국','캐다다']
capital=['브라질리아','워싱턴','오타와']
for num in range(3) :#0 1 2 
    problem=country[num]+'의 수도는'#브라질의 수도는
    answer=input(problem)#브라질리아
    if answer==capital[num]:
        print('대단한데!')
    else:
        print('응아니야', capital[num],'이야')
