a = int(input ('Digite um número: '))
b = int(input ('Digite outro número: '))
c = int(input ('Digite o útimo número: '))

if a>b:
    if a>c:
        if b>c:
            while b<a:
                print(b)
                b = b + 1
                
        else:
            while c<a:
                print(c)
                c = c + 1
                
    else:
        while a<c:
                print(a)
                a = a + 1
else:
    if b>c:
        if c>a:
            while c<b:
                print(c)
                c = c + 1
        else:
            while a<b:
                print(a)
                a = a + 1
    else:
        while b<c:
                print(b)
                b = b + 1
        
