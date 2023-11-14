# Ler dois vetores A e B com nove elementos. Construir um vetor C, na qual cada elemento de
# C é a subtração do elemento correspondente a A com B ou B com A para que o valor da
# subtração fique positivo ou nulo. Ao final, apresentar o vetor C

import random

listaA = []
listaB = []
listaC = []

cont1 = 0
cont2 = 0
cont3 = 0

while(cont1 < 9):
    rand = random.randint(1,100)
    listaA.append(rand)
    cont1 += 1
    
while(cont2 < 9):
    rand2 = random.randint(1,100)
    listaB.append(rand2)
    cont2 += 1

for i in range (9):
 d = listaA[i] - listaB[i]
 if(d > 0):
  listaC.append(d) 
 else:
   d2 = listaB[i] - listaA[i] 
   listaC.append(d2)
  
 
print("Lista A de elementos: ")   
print(listaA)

print("-----------------------------------")

print("Lista B de elementos: ")
print(listaB)

print("-----------------------------------")

print("Lista C de elementos: ")
print(listaC)





