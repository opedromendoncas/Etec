notas= []
x = 3
y = 0
for y in range(x):
    notas.append(eval(input('Digite a 1º nota do aluno: ')))

y = 0

for y in range(len(notas)) :
    print(notas[y]);
    total = total + notas[y]

media = total / len(notas)

print('media: ', media)
