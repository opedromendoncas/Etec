a = int(input ('Digite um número: '))
b = int(input ('Digite outro número: '))
c = int(input ('Digite o útimo número: '))

if a>b:
    if a>c:
        if b>c:
            print(c, b, a)
        else:
            print(b, c, a)
    else:
        print(b, a, c)
else:
    if b>c:
        if c>a:
            print(a, c, b)
        else:
            print(c, a, b)
    else:
        print(a, b, c)
        
