vetor_ano = ["2003", "2013", "2023"]

vetor_modelos = ["Iveco", "Volvo ", "Scania"]


inicio = True
decisao = int(input("-- Pressione 1 para iniciar o programa -- "))


linhas = int(input("Insira quantos anos deseja preencher na matriz:"))
matriz = [[" " for _ in range(len(vetor_modelos))]for _ in range(linhas)]
colunas = len(vetor_modelos)


for j in range(colunas):
    print("---------------------------------------------------------")
    print(f"Insira as quantidades para o modelo [{vetor_modelos[j]}]")
    for i in range(linhas):
        quantidade = int(input(f"Quantidade de ônibus do tipo [{vetor_modelos[j]}] no ano [{vetor_ano[i]}]: "))
        matriz[i][j] = quantidade

print("        ","  ".join(vetor_ano))


for j in range(colunas):
    print(vetor_modelos[j], end = "   " )
    for i in range(linhas):
        print(f"{matriz[i][j]:4}", end = "   ")
    print() 
