# Faça um programa em Python que leia dados de 4 pessoas. Os dados são: nome, idade e
# sexo. Depois mostre a média aritmética das idades, o nome e a idade da pessoa mais velha e
# o nome das mulheres abaixo de 20 anos.


limitador = 4
maior_idade = 0
soma_idades = 0
guarda_nome = ""
media = 0
cont = 0
lista_mulheres_abaixo_de_20 = []

while(cont < limitador):
 print()
 nome = str(input(f"Insira o nome do usuario #{cont} : "))    
 cont += 1
 idade =int(input("Insira a idade: "))
 if idade > maior_idade:
     maior_idade = idade
     guarda_nome = nome
 sexo = str(input("Insira o sexo: f // m -- "))
 if(sexo == "f" and idade < 20):
    lista_mulheres_abaixo_de_20.append(nome) 
 soma_idades += idade
 media = soma_idades/cont


print()
print("Media aritmetica das idades: " , media)  
print("Pessoa mais velha: ", guarda_nome, "Idade: ", maior_idade)  
print("Nome das mulheres com menos de 20 anos: ")
for nome in lista_mulheres_abaixo_de_20:
    print(" - " , nome) 