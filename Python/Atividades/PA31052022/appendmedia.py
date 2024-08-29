notas= []
x = 3
y = 0
for y in range(x):
    notas.append(eval(input('Digite a 1º nota do aluno: ')))

y = 0

for y in range(len(notas)) :
    print(notas[y]);

total = notas[0] + notas[1] + notas[2]

media = total /3
print('media: ', media)
