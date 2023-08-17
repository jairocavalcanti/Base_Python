# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


import math


capacidade_lata_de_tinta = 18;
cobertura_por_litro = 3  
preco = 80;

metrosquadrados = int(input("Insira os metros quadrados a serem pintados: "))

litros_necessarios = (metrosquadrados/cobertura_por_litro)

# "math.ceil" utilizado para arredondar calculo
latas_necessarias = math.ceil(litros_necessarios/capacidade_lata_de_tinta)
preco_total = (latas_necessarias*preco)


print("Litros necessarios: " , litros_necessarios)
print("Latas necessarias: ", latas_necessarias)
print("Preço a ser pago: ", preco_total)