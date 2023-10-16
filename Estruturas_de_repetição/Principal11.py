# Faça um programa em Python que leia duas notas e a matrícula de 50 alunos, calcule e
# imprima:
# a) A média aritmética das notas de cada aluno e uma mensagem indicando se o aluno está
# aprovado ou reprovado, conforme quadro abaixo

import random

cont = 0

while cont < 50:

   nota1 = random.randint(1,10)
   nota2 = random.randint(1,10)
   matricula = random.randint(1,1000)
   cont += 1
   
   print()
   
   media = (nota1 + nota2) / 2
   
   print("#" , cont , "#")
   print("Nota 1: " , nota1)
   print("Nota 2: " , nota2)
   print("Matricula: " , matricula)
   if(media <= 5):
       print("Situação -- REPROVADO ")
   else:
       print("Situação -- APROVADO")