import json

def salvar_estoque(estoque):
    with open("estoque.json", "w") as arquivo:
        json.dump(estoque, arquivo, indent=4)

def carregar_estoque():
    try:
        with open("estoque.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return{}

def verificar_estoque(quantidade):
    if quantidade <= 100:
        return "⚠️ IMPRIMIR FOLHAS"
    return ""

estoque = carregar_estoque()

while True:
    print("\n ======== ESTOQUE DE FOLHAS ========")
    print("1 - Cadastrar Pizzaria")
    print("2 - Consultar Estoque")
    print("3 - Adicionar Folhas")
    print("4 - Remover Folhas")
    print("5 - Remover Pizzaria")
    print("6 - Listar Todas")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome =  input("Nome da Pizzaria: ").title()
        quantidade = int(input("Quantidade de Folhas: "))
        estoque[nome] = quantidade
        salvar_estoque(estoque)
        print("Pizzaria Cadastrada!")
    
    elif opcao == "2":

        busca = input("Digite o nome da pizzaria: ").lower()

        encontrou = False

        for nome, quantidade in estoque.items():
            if busca in nome.lower():      
                aviso =  verificar_estoque(quantidade)
                print(f"{nome} -> {quantidade} folhas {aviso}")
                encontrou = True

        if not encontrou:
            print("Nenhuma pizzaria encontrada.")

        

    elif opcao == "3":
        nome = input("Nome da pizzaria: ").title()
        if nome in estoque:
            adicionar = int(input("Quantas folhas deseja adicionar? "))
            estoque[nome] += adicionar
            salvar_estoque(estoque)
            aviso =  verificar_estoque(quantidade)
            print(f"{nome} agora possui {quantidade} folhas {aviso}")

        
    elif opcao == "4":
        nome = input("Nome da pizzaria: ").title()
        if nome in estoque:
            retirar = int(input("Quantas folhas deseja retirar? "))
            if retirar <= estoque[nome]:
                estoque[nome] -= retirar
                salvar_estoque(estoque)
                aviso =  verificar_estoque(quantidade)
                print(f"Retiradas {retirar} folhas. Estoque atual: {estoque[nome]} folhas {aviso}")
            else:
                print("Não há folhas suficientes.")

       
    elif opcao == "5":
        nome = input("Nome da pizzaria: ").title()
        if nome in estoque:
            del estoque[nome]
            salvar_estoque(estoque)
            print("Pizzaria removida!")
        else:
            print("Pizzaria não encontrada!")

    elif opcao == "6":
        if len(estoque) == 0:
            print("Nenhuma pizzaria cadastrada.")
        else:
            print("\nEstoque:")
            for nome, quantidade in estoque.items():
                aviso =  verificar_estoque(quantidade)
                print(f"{nome} - {quantidade} folhas {aviso}")

        

    elif opcao == "7":
        print("Sistema encerrado!")
        break

    else:
        print("Opção Inválida!")