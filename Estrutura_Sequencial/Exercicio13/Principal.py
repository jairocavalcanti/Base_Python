# Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

print()

altura = float(input("Insira a altura: "))

print("Altura inserida: " , altura)

pesoidealhomens = ((72.7*altura) - 58)
pesoidealmulheres = ((62.1*altura) - 44.7)

print()

print("Altura ideal para homens: " , pesoidealhomens)
print("Altura ideal para mulheres: " , pesoidealmulheres)