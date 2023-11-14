# Escreva um algoritmo que leia um vetor de 50 elementos inteiros. Encontre e mostre o maior
# elemento e sua posição no vetor

import random

vetorA = []

cont = 0
maior_numero = 0 

while(cont < 50):
    cont += 1
    rand = random.randint(1,100)
    vetorA.append(rand)
    if(rand > maior_numero):
        maior_numero = rand
        
print("VetorA: " , vetorA)


posicao_maior_numero = []

for i in range(len(vetorA)):
    if(vetorA[i] == maior_numero):
        posicao_maior_numero.append(i)
        

print()

print("Maior elemento no vetor: " , maior_numero)
print("Posição do maior numero no vetor: " , posicao_maior_numero)