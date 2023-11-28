

matriz = []

linhas = int(input("Insira quantos alunos tera a matriz: "))
coluna = 4

contador = 0
contador_de_notas = 0

for i in range(linhas):
    linha = []
    for j in range(coluna):
        contador = i+1
        notas = float(input(f"insira as notas do aluno {contador}  : [{i}] [{j}] :"))
        linha.append(notas)
        contador_de_notas += notas
       
    matriz.append(linha)
   
print()  
print("----------------------------------")    
print("-- MATRIZ -- ")  
cont = 0

for linha in matriz:
  cont += 1
  print(f"Notas do aluno {cont} :" ,linha)
 
print(contador_de_notas)