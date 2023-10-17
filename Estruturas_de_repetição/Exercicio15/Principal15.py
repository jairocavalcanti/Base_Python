# Faça um programa em Python que leia os dados de cada empregado: matrícula, salário por
# dia e número de dias trabalhados de uma firma. Imprima a matrícula, o salário a ser pago a
# cada empregado, o total da folha de pagamento (total de salários a serem pagos) e a média
# dos salários. O número da matrícula igual a zero deve ser usado para término do programa

import random

cont = 0
soma_salarios = 0
numero_de_salarios = 0

while True:
 print()
 print("-------- FICHA --------")
 cont += 1
 matricula = int(input(f"Insira o numero da matricula #{cont} : "))
 if(matricula == 0):
  break
 salario_por_dia = random.uniform(150,450)
 print(f"Salario diario do funcionario com matricula #{matricula}: {salario_por_dia:.2f}")
 dias = int(input("Insira os dias trabalhados: "))
 salario_a_ser_pago = salario_por_dia*dias
 soma_salarios += salario_a_ser_pago
 print(f"Salario a ser pago ao funcionario: {salario_a_ser_pago:.2f}")
 if(salario_por_dia > 1):
  numero_de_salarios += 1


print("----------------------------------------------------")
 
print("Total de salarios a serem pagos: " , numero_de_salarios)
media_salarios = soma_salarios/cont
print(f"Media salarial:  {media_salarios:.2f}")
 