a = int(input ('Digite um número: '))
b = int(input ('Digite outro número: '))
c = int(input ('Digite o útimo número: '))

if a<b:
    if a<c:
        a=a+5
        print(a)
    else:
        if a==c:
            print("Números iguais")
        else:
            c=c+5
            print(c)
else:
    if b<c:
        b=b+5
        print(b)
    else:
        if b==c:
            print("Números iguais")
        else:
            c=c+5
            print(c)
