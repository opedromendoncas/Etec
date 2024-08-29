x=0
y=0
n=[15,3,20,10]
print("Vetor Original")
print(n)

for y in range(3):
    if n[y]>n[y+1]:
        x=n[y]
        n[y]=n[y+1]
        n[y+1]=x
    print(n)

print("Vetor após interação")    
print(n)
