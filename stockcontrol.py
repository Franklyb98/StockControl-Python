import json
from datetime import datetime

# Função para salvar estoque #
def salvar_estoque(estoque):
    with open("estoque.json", "w") as arquivo:
        json.dump(estoque, arquivo, indent=4)
# Função para carregar o estoque #
def carregar_estoque():
    try:
        with open("estoque.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return{}
# Função para verificar quantidade de folhas #
def verificar_estoque(quantidade):
    if quantidade <= 100:
        return "⚠️ IMPRIMIR FOLHAS"
    return ""
# Função para carregar historico de movimentações #
def carregar_historico():
    try:
        with open("historico.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
# Função para salvar o historico #
def salvar_historico(historico):
    with open("historico.json", "w") as arquivo:
        json.dump(historico, arquivo, indent=4)
# Função para registrar movimentação #
def registrar_movimentacao(nome, tipo, quantidade):
    historico = carregar_historico()
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    movimentacao = {
        "pizzaria": nome,
        "tipo": tipo,
        "quantidade": quantidade,
        "data": data
    }

    historico.append(movimentacao)
    salvar_historico(historico)


estoque = carregar_estoque()
historico = carregar_historico()


while True:
    print("\n ======== ESTOQUE DE FOLHAS ========")
    print("1 - Cadastrar Pizzaria")
    print("2 - Consultar Estoque")
    print("3 - Adicionar Folhas")
    print("4 - Remover Folhas")
    print("5 - Remover Pizzaria")
    print("6 - Listar Todas")
    print("7 - Relatórios")
    print("8 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome =  input("Nome da Pizzaria: ").title()

        if nome in estoque:
            print("⚠️ Essa pizzaria já está cadastrada!")
        else:
               quantidade = int(input("Quantidade de Folhas: "))
               estoque[nome] = quantidade
               salvar_estoque(estoque)
               print("Pizzaria cadastrada com sucesso!")

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
            registrar_movimentacao(nome, "Entrada", adicionar)
            aviso =  verificar_estoque(estoque[nome])
            print(f"{nome} agora possui {estoque[nome]} folhas {aviso}")
      
    elif opcao == "4":
        nome = input("Nome da pizzaria: ").title()
        if nome in estoque:
            retirar = int(input("Quantas folhas deseja retirar? "))
            if retirar <= estoque[nome]:
                estoque[nome] -= retirar
                salvar_estoque(estoque)
                registrar_movimentacao(nome, "Saída", retirar)
                aviso =  verificar_estoque(estoque[nome])
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
        while True:
         
            print("\n ======== RELATÓRIOS  ========")
            print("1 - Total de folhas em estoque")
            print("2 - Total de Cadastros")
            print("3 - Estoque baixos")
            print("4 - Histórico de Movimentação")
            print("5 - Voltar")

            relatorio = input("Escolha uma opção: ")

            if relatorio == "1": 
                total = sum(estoque.values())
                print(f"Total de folhas no estoque: {total}")

            elif relatorio == "2":
                total_cadastros = len(estoque)
                print(f"Quantidade de Cadastros:  {total_cadastros}")

            elif relatorio == "3":
                encontrou = False
                for nome, quantidade in estoque.items():
                    if quantidade <= 100:
                        print(f"{nome} -> {quantidade} folhas ⚠️ IMPRIMIR FOLHAS ")
                        encontrou = True
                if not encontrou:
                    print("Nenhum estoque baixo.")


            elif relatorio == "4":
                historico = carregar_historico()
                if not historico:
                    print("Nenhuma movimentação registrada.")
                else:
                    print("\n ======== HISTÓRICO DE MOVIMENTAÇÕES ========")
                    for movimentacao in historico:

                        print(
                            f"{movimentacao['data']} | "
                            f"{movimentacao['pizzaria']} | "
                            f"{movimentacao['tipo']} | "
                             f"{movimentacao['quantidade']} folhas"
                        )
                        print("\n --------------------------------------------------------")
                           
                        

            elif relatorio == "5":
                break
            else:
                print("Opção inválida!")



    elif opcao == "8":
        print("Sistema encerrado!")
        break

    else:
        print("Opção Inválida!")