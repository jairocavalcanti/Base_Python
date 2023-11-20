# Implementar um algoritmo que calcule e escreva o somatório dos valores armazenados
# numa variável unidimensional A de 100 elementos numéricos a serem lidos do teclado

import random

lista_elementos = []
cont = 0
soma = 0

while(cont < 100):
 rand = random.randint(1,10)
 soma += rand
 cont += 1
 lista_elementos.append(rand)


print(lista_elementos)
print("Soma dos elementos do vetor: " , soma)
