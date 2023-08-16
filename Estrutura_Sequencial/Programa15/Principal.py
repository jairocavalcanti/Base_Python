# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# salário líquido.

print()

ganho = float(input("Insira o seu ganho por hora: "))

horas = float(input("Insira a quantidade de horas trabalhadas no mes: "))

bruto = (ganho*horas)

print("Salario bruto: " , bruto)

IR = (bruto*0.11)
INSS = (bruto*0.08)
SIND = (bruto*0.05)

print()

print("Quantidade paga ao imposto de renda: " , IR)
print("Quantidade paga ao INSS: " , INSS)
print("Quantidade paga ao sindicato: " , SIND)

montante = (IR + INSS + SIND)

print("Quantidade total paga em impostos: " , montante)

salarioliquido = (bruto - montante)

print("Salario liquido: " , salarioliquido)
