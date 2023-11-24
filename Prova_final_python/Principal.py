
vetor = ["Mercedes-Benz O500", "Volvo B7R", "Scania K-series", "MAN Lion's Coach"]

cont = 0
matriz_cheia = False


          #[[" ", " ", " "],
          #[" ", " ", " "],
          #[" ", " ", " "]]



while True:
   programa = True

   print(" ---------------------------------")
   print(" ------ MODELOS DISPONÍVEIS ------ \n",
      "--------------------------------- \n",
      "  #0 - Mercedes-Benz O500  \n",
      "  #1 - Volvo B7R   \n",
      "  #2 - Scania K-series   \n", 
      "  #3 = MAN Lion's Coach   \n",
      "---------------------------------",)

   while programa:
         
         escolha1 = int(input(" -- Pressione 1 para iniciar o programa -- \n"))

         if(escolha1 == 1):
            linhas = int(input("Insira a quantidade de linhas da matriz: "))
            colunas = int(input("Insira a quantidade de colunas da matriz: "))
            matriz = [[" " for _ in range(colunas)] for _ in range(linhas)]
            programa = False
  
   while not programa:
  
    escolha2 = int(input(" -- Insira uma opção: 1 - inserir dados // 2 - Mostrar dados // 3 - alterar dados // 4 - consulta especifica de dados // 0 - Encerrar --"))
  
    if(escolha2 == 0):
      print("Programa encerrado...")
      programa = True
    

    match escolha2:
    
      case 1:
       
       if(matriz_cheia != False):
         print("--------------------------")
         print("Matriz ja preenchida !")
         print("--------------------------")
  
       else:      
      
         for i in range(linhas):
            for j in range(colunas):
                print("")
                elemento = int(input(f"Insira a numeração (correspondente ao nome) do ônibus de posição #[{i}][{j}] da matriz: "))
                matriz[i][j] = vetor[elemento]   
            
         matriz_cheia = True
         print("--------------------------------")
         print("Dados inseridos com sucesso!")
         print("--------------------------------")
    
      case 2:
       
       print()
       
       print("-------------------------- MATRIZ --------------------------")

       cont = 0

       for i in range(linhas):
             print(f"Linha #{i + 1}: ", end='')  
             for j in range(colunas):
                print("[" , matriz[i][j], end = "]")
             print()


       for elemento in matriz:
            print(f"Linha #{cont} -- {elemento}")
       
       print("-------------------------------------------------------------")
      
      case 3:
    
       print("--------------------------------------------------------------------------")
    
       linha2 = int(input("Insira a posição da [LINHA] do elemento: "))
       coluna2 = int(input("Insira a posição da [COLUNA] do elemento: "))
    
       novo_elemento = int(input("Insira o novo valor: "))
    
       matriz[linha2][coluna2] = vetor[novo_elemento]
       
       print("--------------------------------------------------------------------------")
       
      case 4:
       
       print("--------------------------------------------------------------------------")
       
       linha3 = int(input("Insira a posição da [LINHA] do elemento que deseja consultar: "))  
       coluna3 = int(input("Insira a posição da [COLUNA] do elemento que deseja consultar: "))
       
       consulta_elemento = matriz[linha3][coluna3]
       
       print(f"Elemento da posição #[{linha3}][{coluna3}] da matriz: ", consulta_elemento)   
       
       print("--------------------------------------------------------------------------")  
       
       
       
       
       
        #print()
        
        #linha2 = int(input("Insira a posição da linha do elemento: "))
        #coluna2 = int(input("Insira a posição da coluna do elemento: "))
        
       # for i in range(linha2):
         #   for j in range(coluna2):
           #    novo = int(input("Insira: "))
            #   matriz[i][j] = novo
            
            
      

