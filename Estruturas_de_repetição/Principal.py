# Faça um programa que escreve na tela a mesma frase 10 vezes. E depois faça com que o
# programa mostre o número de cada linha no início e no final da linha, conforme exemplo:
# 1 Sou um programa Python! 1
# 2 Sou um programa Python! 2
# 3 Sou um programa Python! 3

cont = 0;
soma = 0;

frase = str(input("Escreva uma frase: "))

while(cont < 10):
 soma += 1
 print("#" , soma , frase)
 cont += 1