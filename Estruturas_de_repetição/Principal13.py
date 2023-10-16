# Faça um programa em Python que leia a altura de 1000 pessoas e imprima a maior, a
# menor, a média destas alturas. Imprima também quantas alturas maiores que 1.60 e quantas
# menores que 1.30

import random

media = 0
cont = 0
maior_altura = 0
menor_altura = 2
maior = 0
menor = 0

while(cont < 1000):
    cont += 1
    altura = random.uniform(1,1.99)
    if altura > maior_altura:
       maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura
    media += altura
    if altura > 1.60:
        maior += 1
    if altura < 1.30:
        menor += 1
        
    
print()    
media2 = media / cont
print(f"Maior altura:  {maior_altura:.2f}")
print(f"Menor altura:  {menor_altura:.2f}")     
print(f"Media das alturas: {media2:.2f}")   
print(f"Alturas maiores que 1.60: {maior}")
print(f"Alturas menores que 1.30: {menor}")
    