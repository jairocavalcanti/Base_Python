# Faça um programa que leia a altura de moças inscritas em um concurso de beleza. Para
# finalizar será digitado zero na altura. Imprima, ao final, a maior altura digitada]

quantidade = 1000

maior_altura = 0
cont = 0


while(cont < quantidade):
    print()
    cont +=1
    escolha = int(input("Inserir altura - 1 // finalizar - 0 : "))
    if escolha == 0:
        break
    else:
     altura = float(input(f"Insira a altura da inscrita # {cont} : "))
     
     # definindo apenas uma variavel para comparação de maior valor, muito útil
     if altura > maior_altura:
        maior_altura = altura
        
print("A maior altura é : " , maior_altura)
         