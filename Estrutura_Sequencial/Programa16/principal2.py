# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

#!! - FORMA ALTERNATIVA PARA RESOLUÇÃO DO PROBLEMA - !!


import math

print()

area = int(input("Insira a area a ser pintada em metros quadrados: "))

print("Area inserida: " , area)

cobertura_latas_de_tinta = 54;
preco_lata_de_tinta = 80;

latas_necessarias = math.ceil(area/cobertura_latas_de_tinta)
preco_a_ser_pago = (latas_necessarias*preco_lata_de_tinta)

print()

print("Latas necessarias: " , latas_necessarias)
print("Preço a ser pago: " , preco_a_ser_pago)

print("")

  