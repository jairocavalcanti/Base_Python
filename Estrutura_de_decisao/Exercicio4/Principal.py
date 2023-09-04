# Faça um Programa que verifique se uma letra digitada é vogal ou consoante

print()

letra = input("Insira uma letra qualquer: ")

# Verificando se a entrada inserida é realmente apenas uma letra
if len(letra) == 1:
    
    # Convertendo entrada para forma minúscula a fim de simplificar o programa
    letra = letra.lower()
    
    # Verificando se a entrada se trata de uma vogal 
    if letra in 'aeiou':
        print("A letra digitada é uma vogal")
    else:
        print("A letra digitada é uma consoante")
else:
    print("Por favor, digite apenas uma letra.")