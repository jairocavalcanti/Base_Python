
vetor_veiculos = ["Mercedes-Benz O500", "Volvo B7R", "Scania K-series", "MAN Lion's Coach 700", "Marcopolo Paradiso 1800 DD G7",
         "Mercedes-Benz O500RSD" ,"Van Hool TDX25 Astromega"," Irizar i8 "," Setra S 431 DT ","MAN Lion's Coach",
         "Temsa Safari HD","Irizar PB","Volvo 9700","Yutong ZK6129H", "Alexander Dennis Enviro500","Neoplan Cityliner",
         "Marcopolo Viaggio G7 1050","Solaris InterUrbino", "VDL Futura FHD2", "MCI J4500" , "Volvo B8R"]

cont = 0
matriz_cheia = False

while True:
   programa = True

   print(" ---------------------------------")
   print(" ------ MODELOS DISPONÍVEIS ------ \n",
      "--------------------------------- \n",
      "  #0  - Mercedes-Benz O50 \n",
      "  #1  - Volvo B7R   \n",
      "  #2  - Scania K-series    \n", 
      "  #3  - MAN Lion's Coach   \n",
      "  #4  - Marcopolo Paradiso 1800 DD G7  \n",
      "  #5  - Mercedes-Benz O500RSD  \n",
      "  #6  - Van Hool TDX25 Astromega  \n",
      "  #7  - Irizar i8  \n",
      "  #8  - Setra S 431 DT  \n",
      "  #9  - MAN Lion's Coach 700  \n",
      "  #10 - Temsa Safari HD \n",
      "  #11 - Irizar PB \n",
      "  #12 - Volvo 9700 \n",
      "  #13 - Yutong ZK6129H \n",
      "  #14 - Alexander Dennis Enviro500 \n",
      "  #15 - Neoplan Cityliner \n",
      "  #16 - Marcopolo Viaggio G7 1050 \n",
      "  #17 - Solaris InterUrbino \n",
      "  #18 - VDL Futura FHD2 \n",
      "  #19 - MCI J4500 \n",
      "  #20 - Volvo B8R \n"
      "---------------------------------",)

   while programa:
         
         escolha1 = int(input(" -- Pressione 1 para iniciar o programa -- \n"))

         if(escolha1 == 1):
            linhas = int(input("Insira a quantidade de linhas da matriz: "))
            colunas = int(input("Insira a quantidade de colunas da matriz: "))
            matriz = [[" " for _ in range(colunas)] for _ in range(linhas)]
            programa = False
  
   while not programa:
  
    print()
    escolha2 = int(input(" -- Insira uma opção: 1 - inserir dados // 2 - Mostrar dados // 3 - alterar dados // 4 - consulta especifica de dados // 0 - Encerrar --  \n"))
   
    if(escolha2 == 0): 
      print("--------------------------")
      print("Programa encerrado...")
      print("--------------------------")
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
                matriz[i][j] = vetor_veiculos[elemento]   
            
                matriz_cheia = True
       print("--------------------------------")
       print("Dados inseridos com sucesso!")
       print("--------------------------------")
    
      case 2:
       
       print()
       
       print("-------------------------- MATRIZ --------------------------")

       cont = 0

       for elemento in matriz:
            print(f"Linha #{cont} -- {elemento}")
            cont += 1
       print("-------------------------------------------------------------")
      
      case 3:
    
       print("--------------------------------------------------------------------------")
       
       if matriz_cheia != False:
  
             linha2 = int(input("Insira a posição da [LINHA] do elemento que deseja alterar: "))
             coluna2 = int(input("Insira a posição da [COLUNA] do elemento que deseja alterar: "))
    
             novo_elemento = int(input("Insira o novo valor: "))
    
             matriz[linha2][coluna2] = vetor_veiculos[novo_elemento]
             print("--------------------------------")
             print(f"Elemento da posição #[{linha2}][{coluna2}] alterado com sucesso!")
             print("--------------------------------")
       else:
         print("Matriz ainda nao preenchida!!")
  
       print("--------------------------------------------------------------------------")
       
      case 4:
       
       print("--------------------------------------------------------------------------")
       
       linha3 = int(input("Insira a posição da [LINHA] do elemento que deseja consultar: "))  
       coluna3 = int(input("Insira a posição da [COLUNA] do elemento que deseja consultar: "))
       
       consulta_elemento = matriz[linha3][coluna3]
       
       print(f"Elemento da posição #[{linha3}][{coluna3}] da matriz: ", consulta_elemento)   
       
       print("--------------------------------------------------------------------------")  
       
       
       

