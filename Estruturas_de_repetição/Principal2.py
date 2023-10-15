# Faça um programa para somar os restos da divisão por 3 de 200 números inteiros digitados
# via teclado

import random;


resto =0
soma_resto = 0 

for i in range(200):
 numero = random.randint(1,1000)
 resto = numero%3
 soma_resto += resto 
    
    
   
print("Soma dos restos: " , soma_resto)