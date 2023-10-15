# Os regulamentos de pesca do Estado de São Paulo impõem um limite no peso total de
# pesca de um dia. Suponha que você planeje levar seu terminal portátil de computador em sua
# próxima pescaria e deseje um programa para calcular quanto você excedeu seu limite.
# Preparar um algoritmo que leia o limite diário (em quilogramas) e, então, leia os valores de
# entrada um por um (os pesos dos peixes à medida que são apanhados) e imprima uma
# mensagem no ponto quando este limite é excedido. Um peso de zero indica o fim de entrada.
# Após o registro de cada peixe, o algoritmo deve imprimir o peso total de peixes obtidos até
# aquele ponto

limite_diario = 200
soma = 0

while True: 
    quantidade = float(input("Insira a quantidade de peixes apanhadas (kg): "))
    if(quantidade == 0):
        break
    soma += quantidade
    if soma >= limite_diario:
        print("----------------------------------------")
        print("Limite excedido, retorne para a costa ! ")
        break
     
    print(f"Peixes apanhados até o momento (kg): {soma} ")
    
    print()
    
print(f"Total de peixes apanhados: {soma} ")