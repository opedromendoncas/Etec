continua = 's'
notas = []

while (continua =='s' or continua=='S') :
    nota = eval(input("Digite uma nota: "))
    notas.append(nota)
    continua = input("Deseja continuar? (s/n): ")

print(notas)

for i in range(len(notas)):
    print(notas[i])

    




