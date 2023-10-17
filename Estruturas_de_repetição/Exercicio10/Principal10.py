# Escreva um programa em Python que leia um número inteiro positivo n e exiba a sequência
# de Fibonacci até o n-ésimo termo. A sequência de Fibonacci é uma sequência numérica em
# que cada termo é a soma dos dois termos anteriores, começando em 0 e 1. Por exemplo, os
# primeiros 10 termos da sequência de Fibonacci são:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

numero = int(input("Insira um número: "))

a, b = 0, 1
cont = 0

print(a)
print(b)

while cont < numero:
    print(a, end=' ')
    # 0 , 1 = 1 , 0 + 1 
    a, b = b, a + b 
    cont += 1