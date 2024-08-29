a = int(input ('Digite um número: '))
b = int(input ('Digite outro número: '))


if a<b:
    a = a + 5
else:
    b = b + 5

if a>b:
    print(a)
else:
    if a==b:
        print("Números iguais.")
    else:
        print(b)
        
