# Uma empresa de calçados está fazendo uma promoção nos preços de seus produtos. Se
# um cliente comprar até 2 calçados, tem o desconto de 5% e se o cliente comprar mais de 3
# calçados, o desconto é de 15%.
# Faça um programa para ler o número de calçados que um cliente está comprando e calcule o
# valor que ele deve pagar com o desconto. Cada calçado tem preço único de R$49,90

quantidade = int(input("Insira a quantidade de calçados a serem comprados: "))

cont = 0 
preco = 49.90

while(cont < quantidade):
  cont +=1
  final = preco*quantidade 
  if(quantidade <= 2):
    desconto1 = (5/100)*final
    valor_final = final - desconto1
    print("Valor final a ser pago: " , valor_final)
    break
  if(quantidade >= 3):
    desconto2 = (15/100)*final
    valor_final2 = final - desconto2
    print("Valor final a ser pago: " , valor_final2)
    break