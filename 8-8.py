a=input("숫자")
a=int(a)
b=input("숫자")
b=int(b)
op=input("+,-,*")
if op== "+":
    c=a+b
elif op=="-":
    c=a-b
elif op=="*":
    c=a*b
elif op=="/":
    c=a/b
else :
    c='error'
print(c)


