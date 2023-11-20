# 6. Um armazém trabalha com 10 mercadorias diferentes. As informações são guardadas em 3
# vetores. O primeiro tem o nome do produto, o segundo tem a quantidade do produto e o
# terceiro tem o preço. Veja o modelo abaixo.
# O dono da loja deseja saber o valor de faturamento de cada mercadoria. Para calcular o
# faturamento de cada mercadoria, use a formula: faturamento = quantidade * preço.
# Ao final, o dono também quer saber o valor total de faturamento de todas as mercadorias.

produto = ["Papel cartolina", "Caderno" , "Lapis" , "Lapiseira" , "Papel A4", "Caneta" , "Controle PS4" , "Controle XBOX", "Mouse" , "MousePad" ]
quantidade = [300, 50, 100, 200, 400, 190, 40, 50, 120, 90]
preco_unitario = [1.50 , 14.90, 0.70, 1.80, 0.40, 1.00, 120.00, 121.00, 30.50, 10.00]
faturamento = 0

faturamento_total_final = 0 

print()

print("Faturamento possivel de cada mercadoria: ")
for i in range(len(produto)):
    faturamento = quantidade[i] * preco_unitario[i]
    print(produto[i] , ":" , faturamento )
    faturamento_total_final += faturamento
    print("--")
    
    
print("Faturamento final com a venda de todas as mercadorias: " , faturamento_total_final)