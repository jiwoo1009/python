import random
import datetime
a=''

alp=["A","B","C","D","E","F","G"]

r=random.choice(alp)#D

for i in alp:#A B C D E
print(a)
st=datetime.datetime.now()
ans=input("빠진 알파벳은?")
if ans==r:
    print("정답입니다")
    et=datetime.datetime.now()
    print((et - st).seconds)
else:
    print("틀렸습니다")
