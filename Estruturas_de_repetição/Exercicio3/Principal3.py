# Faça um programa que pede ao usuário a digitação de números inteiros até que este
# introduza o número -1. O programa deve mostrar a média dos números introduzidos (excluindo
# o número -1

cont = 0
media = 0

while True:
  numero = int(input("Insira um numero: "))
  if(numero == -1):
      break
  cont += 1
  media += numero
  media2 = media / cont
  
  
print("media do numeros digitados (excluindo o -1): " , media2)
  
  
    