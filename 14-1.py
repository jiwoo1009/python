import random
def make_question( ):    
    a=random.randint(1,40)#1
    b=random.randint(1,20)#2
    op=random.randint(1,3)#1

    q=str(a)#'1'

    if op==1:
        q=q+ "+"#1+
    if op==2:
        q=q+"-"
    if op==3:
        q=q+"*"
    q = q+str(b)#'1+2'
    return(q)
sc1=0
sc2=0

for x in range(5):
    q=make_question( )#'1+2'
    print(q)

    ans=input("?")
    r=int(ans)

    if eval(q) ==r:#eval('1+2')
        print("정답")
        sc1= sc1+1
    else:
        print("오답")
        sc2=sc2+1
print("정답:",sc1,"오답:",sc2)
if sc2 ==0:
    print("당신은 천재입니다!")
            
