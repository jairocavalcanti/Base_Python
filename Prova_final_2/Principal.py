vetor_ano = ["2003", "2013", "2023"]
vetor_modelos = ["Iveco", "Volvo", "Scania"]
ini_2 = False

while True:
    decisao = int(input("-- Pressione 1 para iniciar o programa -- "))
    colunas = int(input("Insira quantas colunas deseja preencher na matriz: (1 á 3)"))
    linhas = len(vetor_modelos)
    matriz = [[" " for _ in range(linhas)] for _ in range(colunas)]
    ini = False
    matriz_cheia2 = False
   
    while not ini:
        print("Opções de operação com a matriz: 1 - Inserir dados // 2 - Mostrar dados // 3 - Alterar elemento // 0 - Encerrar programa")
        opcoes = int(input(" -- Insira uma opção de operação com a matriz: "))

        match opcoes:
            case 0:
                ini = True
                print("--------------------------")
                print("Programa encerrado...")
                print("--------------------------")

            case 1:
                for j in range(linhas):
                    print("---------------------------------------------------------")
                    print(f"Insira as quantidades para o modelo [{vetor_modelos[j]}]")
                    for i in range(colunas):
                        quantidade = int(input(f"Quantidade de ônibus do tipo [{vetor_modelos[j]}] no ano [{vetor_ano[i]}]: "))
                        matriz[i][j] = quantidade

            case 2:
                matriz_cheia = True
                for j in range(linhas):
                    for i in range(colunas):
                        if matriz[i][j] == " ":
                            matriz_cheia = False
                            break

                    if not matriz_cheia:
                        print("--------------------------")
                        print("Matriz ainda não preenchida!")
                        print("--------------------------")
                        break
                    else:
                        print()
                        print("---------------- MATRIZ ----------------")
                        matriz_cheia2 = True
                        print("--------------------------")
                        print("        ", "  ".join(vetor_ano))
                        for j in range(linhas):
                            print(vetor_modelos[j], end="   ")
                            for i in range(colunas):
                                print(f"{matriz[i][j]:^4}", end="   ")
                            print()
                            print("--------------------------")
                    break
            case 3:
               
                if matriz_cheia2:
                  coluna = int (input("Insira o numero da coluna que deseja alterar: "))
                  linha = int(input("Insira o numero da linha que deseja alterar na matriz: "))
                  
                  
                  nova_quantidade = int(input(f"Insira a nova quantidade da posição {linha}{coluna} :"))
                  
                  matriz[linha][coluna] = nova_quantidade
                  
                  print("--------------------------")
                  print("Elemento alterado com sucesso!")
                  print("--------------------------")
                    
                
                else:
                     print("--------------------------")
                     print("Matriz ainda não preenchida!")
                     print("--------------------------")
                    
                    
                  
                   
                 
                 
                  
                 