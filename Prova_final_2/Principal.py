vetor_ano = ["2003", "2013", "2023"]
vetor_modelos = ["Iveco", "Volvo", "Scania"]
ini_2 = False

while True:
    print()
    print("// -- Programa para gerenciamento de dados em uma matriz python -- //")
    print("Escrito por: Jairo , Arthur")
    print("---------------------------")
    decisao = int(input("-- Pressione 1 para iniciar o programa -- \n"))
    colunas = 3
    linhas = len(vetor_modelos)
    matriz = [[" " for _ in range(linhas)] for _ in range(colunas)]
    ini = False
    matriz_cheia2 = False
   
    while not ini:
        print("Opções de operação com a matriz: 1 - Inserir dados // 2 - Mostrar dados // 3 - Alterar elemento // 4 - Buscar elemento especifico // 0 - Encerrar programa")
        opcoes = int(input(" -- Insira uma opção de operação com a matriz: "))

        match opcoes:
           
            case 0:
              
                ini = True
                print("--------------------------")
                print("Programa encerrado...")
                print("--------------------------")

            case 1:
                
                for j in range(linhas):
                    for i in range(colunas):
                        if matriz[0][0] != " ":
                            matriz_cheia_3 = True
                            break
                        else:
                            matriz_cheia_3 = False
                            break
               
                if not matriz_cheia_3:
                   for j in range(linhas):
                      print("---------------------------------------------------------")
                      print(" -- Pressione 0 para encerrar o preenchimento -- ")
                      print()
                      print(f"Insira as quantidades para o modelo [{vetor_modelos[j]}]")
                      for i in range(colunas):
                        quantidade = int(input(f"Quantidade de ônibus do tipo [{vetor_modelos[j]}] no ano [{vetor_ano[i]}]: "))
                        if quantidade == 0:
                            break
                        else:                           
                         matriz[i][j] = quantidade
                         matriz_cheia2 = True
                   print("---------------------------------------------------------------")
                else:
                    print("--------------------------")
                    print("Matriz ja preenchida!")        
                    print("--------------------------")    
            
            case 2:
              
                matriz_cheia = True
                for j in range(linhas):
                    for i in range(colunas):
                        if matriz[i][j] == " ":
                            matriz_cheia = False
                            break

                    if not matriz_cheia2:
                        print("--------------------------")
                        print("Matriz ainda não preenchida!")
                        print("--------------------------")
                        break
                    else:
                        print()
                        print("---------------- MATRIZ ----------------")
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
                  print("---------------------------------------------------------------")
                  coluna = int (input("Insira o numero da [coluna] que deseja alterar na matriz: "))
                  linha = int(input("Insira o numero da [linha] que deseja alterar na matriz: "))
                  
                  
                  nova_quantidade = int(input(f"Insira a nova quantidade da posição Linha: [{linha}][{vetor_modelos[linha]}] Coluna: [{coluna}][{vetor_ano[coluna]}] da matriz :"))
                  
                  matriz[coluna][linha] = nova_quantidade
                  
                  print("--------------------------")
                  print("Elemento alterado com sucesso!")
                  print("--------------------------")
                  
                  print("---------------------------------------------------------------")  
                
                else:
                     print("--------------------------")
                     print("Impossivel alterar, Matriz ainda não preenchida!")
                     print("--------------------------")
            
            case 4: 
               
               if matriz_cheia2:
                 print("---------------------------------------------------------------")
                 coluna = int (input("Insira o numero da [coluna] que deseja buscar na matriz: "))
                 linha = int(input("Insira o numero da [linha] que deseja buscar na matriz: "))      
                
                 elemento = matriz[coluna][linha]
                 
                 print(f"Elemento da posição Linha: [{linha}][{vetor_modelos[linha]}] Coluna: [{coluna}][{vetor_ano[coluna]}] da matriz: " , elemento)
                 print("---------------------------------------------------------------")
            
               else:
                     print("--------------------------")
                     print("Impossivel buscar, Matriz ainda não preenchida!")
                     print("--------------------------") 
                
                
                
                
                        
                  
                   
                 
                 
                  
                 