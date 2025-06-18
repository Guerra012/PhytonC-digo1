print("Olá! Vamos cadastrar roupas")

roupas=[]
quantidade_roupas = 5

for i in range(1, quantidade_roupas + 1):
    tipo_roupas = input (f"Digite o tipo de roupa{i}:")
    cor  = input (f"Digite a cor da roupa{i}: ")
    roupas.append ({"tipo_roupas": tipo_roupas, "Cor": cor})

opcao = input ("Roupas cadastradas com sucesso! Deseja exibir o estoque completo? (s/n):").strip().lower()

if opcao == 's':
    print("\nEstoque de roupas cadastrados:")
    for idx, roupa in enumerate (roupas, start=1):
        print (f"{idx} Tipo: {roupa ['tipo_roupas']} | Cor: {roupa ['Cor']}")
else:
        print ("Ok! Encerrando o estoque")
