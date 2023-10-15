# Faça um programa para calcular o fatorial de um número qualquer. Os passos são: inicie as
# variáveis fatorial e contador com o valor 1; solicite o valor de um número para calcular a seu
# fatorial; multiplique sucessivamente a variável fatorial pela variável contador; incrementar 1 à
# variável contador, efetuando o controle até o valor solicitado; Apresentar ao final o valor obtido

fatorial = 1
contador = 1

numero = int(input("Insira o numero para se calcular o fatorial: "))

# FATORIAL: 

# 0 = 1
# 1 = 1
# 2 = 2 x 1
# 3 = 3 x 2 x 1
# 4 = 4 x 3 x 2 x 1
# 5 = 5 x 4 x 3 x 2 x 1



while(contador <= numero):
 fatorial *= contador
 contador += 1
 
 print("Fatorial: " , fatorial)

    