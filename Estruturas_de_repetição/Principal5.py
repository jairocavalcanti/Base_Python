# Apresentar todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20. Para
# verificar se o número é ímpar efetue a verificação dentro do loop. Caso o número seja ímpar,
# mostre-o, não sendo, passe para o próximo número

cont = 0
numero = 20

print("Numeros impares de 0 á 20:")

while(cont < numero):
   cont+=1
   if cont % 2 == 1: 
    # "end" ao fim da linha indica que tudo sera impresso nessa mesma linha, juntamente com o elemento string passado a direita 
    print(cont ,  end= " - ")
   

        
