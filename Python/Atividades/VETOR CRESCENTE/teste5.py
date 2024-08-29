continua = 's'
n = []

while (continua =='s' or continua=='S') :
    ns = eval(input("Digite uma nota: "))
    n.append(ns)
    continua = input("Deseja continuar? (s/n): ")

w=len(n)-1
x=0
y=0
troca=1

print("Vetor Original")
print(n)

while troca==1 :
    troca=0
    y=0
    
    for y in range(w):
        if n[y]>n[y+1]:
            x=n[y]
            n[y]=n[y+1]
            n[y+1]=x
            troca=1
        print(y, n)

print("Vetor após interação")    
print(n)
