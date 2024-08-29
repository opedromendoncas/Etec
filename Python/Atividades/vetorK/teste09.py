continua = 's'
notas = []

while (continua =='s' or continua=='S') :
    nota = eval(input("Digite uma nota: "))
    notas.append(nota)
    continua = input("Deseja continuar? (s/n): ")

maior = 0

for i in range(len(notas)):
    if notas[i]> maior:
        maior=notas[i]

print("A maior nota informada foi:", maior)

        
    

    




