
alf=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,w,z]

while (continua =='s' or continua=='S') :
    ns = eval(input("Digite uma nota: "))
    p.append(ns)
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
        if p[y]>p[y+1]:
            x=p[y]
            p[y]=p[y+1]
            p[y+1]=x
            troca=1
        print(y, n)

print("Vetor após interação")    
print(n)

