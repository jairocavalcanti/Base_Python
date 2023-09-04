# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
 
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual ou maior que dez

nota1 = float(input("Insira a primeira nota do aluno: "))

nota2 = float(input("Insira a segunda nota do aluno: "))

media = (nota1 + nota2)
media2 = media / 2

if media2 == 10:
    print(" -- !! Aprovado com distinção !! --")
elif media2 >= 7:
    print(" -- Aprovado --")
else:
    print(" -- Reprovado --")
