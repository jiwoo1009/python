def hap(a ):
    s=0
    for x in range(1,a+1):
        s=s + x
    print('1부터', a, '까지 합은', s)

a=input('수를 입력하세요.')
a=int(a)
hap(a)
