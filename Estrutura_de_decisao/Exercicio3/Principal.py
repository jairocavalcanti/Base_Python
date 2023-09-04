# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido

print()

# 'input' reconhece o tipo String automaticamente
sexo = input("Insira o sexo: F - feminino // M - masculino:  \n")

# Converte a letra para maiúscula para evitar diferenciação
sexo = sexo.upper()


if(sexo == "F"):
    print("Sexo FEMININO identificado !")

elif(sexo == "M"):
    print("Sexo MASCULINO identificado !")

else:
    print("Sexo nao identificado !!")
 
 