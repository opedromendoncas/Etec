notas= []
x = 3
y = 0
while y< x :
    notas.append(eval(input('Digite a 1º nota do aluno: ')))
    y = y +1;
print(notas)

while y< x :
    print(notas[y]);
    y = y +1;


x = len(notas);
y = 0;

while y< x :
    print(notas[y]);
    y = y +1;

for y in range (x) :
    print(notas[y]);

