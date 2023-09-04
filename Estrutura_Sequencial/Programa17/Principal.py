# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro 
# para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem 
# compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
# considere latas cheias.

import math

print()

metros_quadrados = float(input("Insira os metros quadrados a serem pintados: "))

print()

alcance_lata_de_tinta = 108
alcance_galao_de_tinta = 21.6;
alcance_tintas_mescladas = 142.56;

quantidade_latas_de_tinta = math.ceil(metros_quadrados/alcance_lata_de_tinta)
quantidade_galoes_de_tinta = math.ceil(metros_quadrados/alcance_galao_de_tinta)
tintas_mescladas = math.ceil(metros_quadrados/alcance_tintas_mescladas)

print("Quantidade de LATAS para cobrir a area inserida: " , quantidade_latas_de_tinta)
print("Quantidade de GALÕES para cobrir a area inserida: " , quantidade_galoes_de_tinta)
print("Quantidade tintas MESCLADAS: " , tintas_mescladas)

print()

preco_latas_de_tinta = (quantidade_latas_de_tinta*80)
preco_galoes_de_tinta = (quantidade_galoes_de_tinta*25)
preco_tintas_mascladas = (tintas_mescladas*105)

print("Preço a ser pago pelas LATAS de tinta: " , preco_latas_de_tinta , "R$ ")
print("Preço a ser pago pelos GALOES de tinta: " , preco_galoes_de_tinta , "R$ ")
print("Preco a ser pago pela tinta MESCLADA: " , preco_tintas_mascladas, "R$ ")

