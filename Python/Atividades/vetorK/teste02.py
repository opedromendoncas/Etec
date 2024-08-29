notas= []
notas.append(eval(input("Digite a nota 1 aluno:")))
notas.append(eval(input("Digite a nota 2 aluno:")))
notas.append(eval(input("Digite a nota 3 aluno:")))
print(notas)

x = len(notas);
y = 0;

while y< x :
    print(notas[y]);
    y = y + 1;

for y in range(x) :
    print(notas[y]);
