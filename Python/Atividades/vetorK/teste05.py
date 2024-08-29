notas= []
total = 0
media = 0
x = 3
y = 0

for y in range(x):
    notas.append(eval(input("Digite a nota 1 aluno:")))

y = 0;

for y in range (len(notas)):
    print('Nota', y, ':', notas[y]);
    total = total + notas[y];

media = total / len(notas)

print ('media',media)




    




