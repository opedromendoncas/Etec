a = int(input ('Digite um número: '))
b = int(input ('Digite outro número: '))
c = int(input ('Digite o útimo número: '))

if a>b:
    if a>c:
        if b>c:
            me=b
            ma=a
        else:
            me=c
            ma=a
    else:
        me=a
        ma=c

else:
    if b>c:
        if c>a:
            me=c
            ma=b
        else:
            me=a
            ma=b
    else:
        me=b
        ma=c

me = me + 1
while me<ma:
    print (me)
    me = me + 1
    
