eleitores = int(input("insira o numero de vezes a ser votado: "))

cont = 0
candidato1 = 0
candidato2 = 0
candidato3 = 0
nulo = 0
branco = 0

while(cont < eleitores):
    cont +=1
    escolha = int(input("Insira a opçao de voto (1 , 2 , 3) , 0 para branco 4 para nulo:"))
    if(escolha == 1):
        candidato1 += 1
    if(escolha == 2):
        candidato2 += 1
    if(escolha == 3):
        candidato3 += 1   
    if(escolha == 0):
        branco += 1
    if(escolha == 4):
        nulo += 1     

print()

print("Numero de votos do candidato 1: " , candidato1)
print("Numero de votos do candidato 2: " , candidato2)
print("Numero de votos do candidato 3: " , candidato3)


#if(candidato1 > candidato2 > candidato3):
   #  print("Candidato com mais votos (candidato1): " , candidato1)
#if(candidato2 > candidato1 > candidato3):
   #  print("Candidato com mais votos (candidato2): " , candidato2)
#if(candidato3 > candidato1 > candidato2):
   #  print("Candidato com mais votos (candidato3): " , candidato3)

print()

print("Numero de votos brancos: " , branco)
print("Numero de votos nulos: " , nulo)

