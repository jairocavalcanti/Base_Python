# 5. Dado um vetor com 80 letras, escreva um algoritmo para:
# a) contar quantas vezes apareceu a letra "A". Se a letra "A" não estiver no vetor, informe ao usuário;
# b) contar quantas vezes ocorre um mesmo par de letras no vetor e quais são elas. Par de letra
# é quando letras iguais estão em posições sequenciais.

import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vetor = []
vetor2 = []
cont = 0
cont2 = 0
cont3 = 0
letra_sequencia = ""

while(cont < 80):
    cont += 1
    letra_aleatorio = random.choice(letras)
    vetor.append(letra_aleatorio)
        
    
print(vetor)    

for i in range(len(vetor)):
    if(vetor[i] == "a"):
        cont2 += 1

for i in range(len(vetor) - 1):
    if(vetor[i] == vetor[i+1]):
      cont3 += 1
      letra_sequencia = vetor[i]
      vetor2.append(letra_sequencia)  
    
print("")      

if(cont2 == 0):
     print("Letra a nao existe no vetor!")
else:
    print("Quantidade de vezes que a letra ","a"," apareceu no vetor: " , cont2)

print("Quantidade de sequencias de letras : " , cont3)
print(vetor2) 
