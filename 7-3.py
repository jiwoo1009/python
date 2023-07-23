import time
import random
count=0
input("자..준비가 되었나요...총 문제는 5문제입니다. 준비가 되면 엔터키를 누르세요!")
start= time .time( )
for x in range(5):
    a=random.randint(1,20)
    b=random.randint(1,20)
    print(a,'+',b,'=')
    k=int(input('정답은? ') )
    if k==a+b:
        count=count+1
end=time.time( )
et=end-start
print(et, "초가 걸렸군요.....", "맞은 개수는" , count)
        
