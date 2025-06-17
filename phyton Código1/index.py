print("Olá! Vamos cadastrar roupas")

roupas=[]
quantidade_roupas=20

for i in range(1, quantidade_roupas+1):
    tiporoupa = input (f"Digite o tipo de roupa{i}:")
    cor  = input (f"Digite a cor da roupa{i}:")
    roupas.append ({"tiporoupa": tiporoupa, "Cor": cor})

OPCAO = input ("Roupas cadastradas com sucesso! Deseja exibir o estoque completo (s/n):"). strip (). lower()

if OPCAO == 's':
    print("\n Estoque de roupas cadastrados:")
    for idx, roupa in enumerate (roupas, start=1):
        print (f"{idx} tiporoupa: {roupa ['tiporoupa']} /cor: {tiporoupa['cor']}")
    else:
        print ("Ok! Encerrando o estoque")