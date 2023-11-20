# Leia cem números pares fornecidos pelo usuário, armazene-os em um vetor A e gere um
# vetor B com o resultado de cada número elevado a 3. O usuário poderá fornecer qualquer
# número, mas deverão ser considerados apenas os pares

import random

listaA = []
listaB = []
cont = 0

print()

while(cont < 100):
 rand = random.randint(1,100)
 if(rand % 2 == 0):
    listaA.append(rand)
 calc = rand ** 3
 listaB.append(calc)
 cont += 1

print("Lista apenas com numeros pares: " , listaA)

print()

print("Resultado de cada numero para elevado a tres: " , listaB)