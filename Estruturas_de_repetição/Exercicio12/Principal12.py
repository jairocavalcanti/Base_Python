# Faça um programa em Python que leia a altura, o sexo(“M”, “F”) e idade de 100 pessoas.
# Calcular e imprimir:
# a) A maior altura;
# b) Quantas mulheres estão com altura maior ou igual a 1.70;
# c) Média de altura das mulheres com mais de 30 anos

import random
       # if altura > maior_altura:
       # maior_altura = altura
media2 = 0
media = 0
cont = 0
maior_altura = 0
maior_altura2 = 0
mulherestrinta = 0

while(cont < 100):
    print()
    cont += 1
    sexo = random.randint(0,1)
    if(sexo == 1):
        print("Sexo: -- M")
    else:
        print("Sexo: -- F")
    altura = random.uniform(1.40,1.80)
    if altura > maior_altura:
        maior_altura = altura
    if altura >= 1.70 and sexo < 1:
        maior_altura2 +=1
    altura_formatada = f'{altura:.2f}'
    idade = random.randint( 18, 90)
    if idade > 30 and sexo < 1: 
        mulherestrinta += 1
        media += altura
    print(f"Dados do individuo #{cont}")
    print("Altura: -- ", altura_formatada)
    print("Idade: -- " , idade)
    
    print()
   
print(f"Maior altura registrada: {maior_altura:.2f}")
print(f"Mulheres com altura maior ou igual a 1.70: {maior_altura2}")
if(mulherestrinta >= 1):
 media2 = media/mulherestrinta
 print(f"Media de altura das mulheres com mais de 30: {media2:.2f}")