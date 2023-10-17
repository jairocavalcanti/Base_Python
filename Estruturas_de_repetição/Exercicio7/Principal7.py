# Escrever um algoritmo que leia um conjunto de valores e calcule a média aritmética dos
# valores lidos, a quantidade de valores positivos e o percentual de valores negativos. Mostre os
# resultados no final. Para terminar o programa, o usuário deverá digitar o valor zero. O valor
# zero não entra nos cálculos

cont = 0
soma = 0
VP = 0
VN = 0

while True:
    cont += 1
    numero = int(input(f"insira o numero # {cont} : "))
    if numero > 0 :
        VP += 1
    elif numero < 0 :
        VN += 1
    elif numero == 0 :
        break        
    soma += numero


media = soma / cont
    
print()
    
print("Quantidade de valores positivos: " , VP)
print("Quantidade de valores negativos: " , VN )
print("Media dos valores inseridos (sem contar o 0): ", media)

total_numeros = VP + VN
percentual_negativos = (VN / total_numeros) * 100

print("Percentual de numeros negativos no conjunto: " , percentual_negativos , "%")