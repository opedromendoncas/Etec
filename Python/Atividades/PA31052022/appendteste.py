notas= []
notas.append(eval(input('Digite a 1º nota do aluno: ')))
notas.append(eval(input('Digite a 2º nota do aluno: ')))
notas.append(eval(input('Digite a 3º nota do aluno: ')))
notas.append(eval(input('Digite a 4º nota do aluno: ')))
print(notas)

print(notas[1])

print(len(notas))

x = len(notas);
y = 0;
while y< x :
    print(notas[y]);
    y = y +1;
    
