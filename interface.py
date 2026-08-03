import customtkinter as ctk
import json
from stockcontrol import *

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

def salvar_estoque(estoque):
    with open("estoque.json", "w") as arquivo:
        json.dump(estoque, arquivo, indent=4)


def carregar_estoque():
    try:
        with open("estoque.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
        

estoque = carregar_estoque()


# ---------------- JANELA PRINCIPAL ----------------

app = ctk.CTk()

app.title("StockControl")
app.geometry("1000x600")


# ---------------- FRAMES ----------------

menu_frame = ctk.CTkFrame(
    app,
    width=200
)

menu_frame.pack(
    side="left",
    fill="y"
)


main_frame = ctk.CTkFrame(app)

main_frame.pack(
    fill="both",
    expand=True
)


# ---------------- FUNÇÕES DOS BOTÕES ----------------

def limpar_tela():
    for widget in main_frame.winfo_children():
        widget.destroy()

def abrir_cadastro():
    limpar_tela()

    titulo = ctk.CTkLabel(
        main_frame,
        text="Cadastro de Pizzaria"
    )
    titulo.pack(pady=20)

    nome_entry = ctk.CTkEntry(
        main_frame,
        placeholder_text="Nome da pizzaria"
    )
    nome_entry.pack(pady=10)

    quantidade_entry = ctk.CTkEntry(
        main_frame,
        placeholder_text="Quantidade de folhas"
    )
    quantidade_entry.pack(pady=10)
    mensagem = ctk.CTkLabel(
                    main_frame,
                    text=""
                )
    mensagem.pack(pady=10)

    def salvar():
            nome = nome_entry.get().strip().title()
            quantidade = int(quantidade_entry.get())

            if nome == "":
                mensagem.configure(text="Digite o nome da pizzaria")
                return
    
            estoque[nome] = quantidade
            salvar_estoque(estoque)

           
            mensagem.configure(
                text="Pizzaria cadastrada com sucesso!"
            )
            mensagem.after(
                2500,
                lambda: mensagem.configure(text="")
            )

           

            if nome in estoque:
                mensagem.configure(
                    text="⚠️ Pizzaria já cadastrada!"
                )
                return

    botao_salvar = ctk.CTkButton(
        main_frame,
        text="Cadastrar",
        command=salvar
    )
    botao_salvar.pack(pady=20)
   
def abrir_consulta():
    limpar_tela()

    titulo = ctk.CTkLabel(
        main_frame,
        text="Consulta de Estoque"
    )
    titulo.pack(pady=20)

    busca_entry = ctk.CTkEntry(
        main_frame,
        placeholder_text="Digite o nome da pizzaria"
    )
    busca_entry.pack(pady=10)

    resultado = ctk.CTkLabel(
        main_frame,
        text="",
        justify="left"
    )
    resultado.pack(pady=10)

    def buscar():
        busca = busca_entry.get().strip().lower()

        resultados = ""

        for nome, quantidade in estoque.items():
            if busca in nome.lower():
                resultados += f"{nome} - {quantidade} folhas\n"

        if resultados == "":
            resultado.configure(
            text="Nenhuma pizzaria encontrada."
        )
        else:
            resultado.configure(
            text=resultados
        )
    
    botao_buscar = ctk.CTkButton(
        main_frame,
        text="Buscar",
        command=buscar
    )
    botao_buscar.pack(pady=20)

def abrir_listar_todas():
    limpar_tela()

    titulo = ctk.CTkLabel(
        main_frame,
        text="📋 Todas as Pizzarias",
        font=("Arial", 22, "bold")
    )
    titulo.pack(pady=20)

    estoque = carregar_estoque()

    lista_frame = ctk.CTkScrollableFrame(
        main_frame
    )
    lista_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    if not estoque:
        ctk.CTkLabel(
            lista_frame,
            text="Nenhuma pizzaria cadastrada."
        ).pack(pady=20)
        return

    for nome, quantidade in estoque.items():
        if quantidade <=100:
            cor = "red"
        else:
            cor = "white"

        card = ctk.CTkFrame(lista_frame)
        card.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ctk.CTkLabel(
            card,
            text=f"🍕 {nome}",
            text_color=cor,
            font=("Arial",18, "bold"),
        ).pack(
            anchor="w",
            padx=15,
            pady=(10,5)
        )

        ctk.CTkLabel(
            card,
            text=f"📦 {quantidade} folhas",
            text_color=cor,
            font=("Arial",15)
        ).pack(
            anchor="w",
            padx=15,
            pady=(0,10)
        )

def abrir_entrada():
    limpar_tela()

    titulo = ctk.CTkLabel(
        main_frame,
        text="Entrada de Folhas"
    )
    titulo.pack(pady=20)

    nome_entry = ctk.CTkEntry(
        main_frame,
        placeholder_text="Nome da pizzaria"
    )
    nome_entry.pack(pady=10)

    quantidade_entry = ctk.CTkEntry(
        main_frame,
        placeholder_text="Quantidade de folhas"
    )
    quantidade_entry.pack(pady=10)

    mensagem = ctk.CTkLabel(
        main_frame,
        text=""
    )
    mensagem.pack(pady=10)

    

    def adicionar():

        estoque = carregar_estoque()
        
        nome = nome_entry.get().strip().title()
        quantidade = quantidade_entry.get().strip()

        if nome == "":
            mensagem.configure(
                text="Digite o nome da pizzaria"
            )
            return
        if quantidade == "":
            mensagem.configure(
                text="Digite a quantidade"
            )
            return
        try:
            quantidade = int(quantidade)
        except ValueError:
            mensagem.configure(
                text="Digite apenas números."
            )
            return
        

        if nome not in estoque:
            mensagem.configure(
                text="Pizzaria não encontrada."
            )
            return

        estoque[nome] += quantidade

        salvar_estoque(estoque)

        registrar_movimentacao(
            nome,
            "Entrada",
            quantidade
        )

        nome_entry.delete(0, "end")
        quantidade_entry.delete(0, "end")

        mensagem.configure(
            text="✅ Entrada registrada com sucesso!"
        )

        mensagem.after(
            2000,
            lambda: mensagem.configure(text="")
        )


    botao_entrada = ctk.CTkButton(
        main_frame,
        text="Adicionar",
        command=adicionar
        )
    botao_entrada.pack(pady=20)    

def abrir_saida():
    limpar_tela

    titulo = ctk.CTkLabel(
        main_frame,
        text="Saída de Folhas"
    )
    titulo.pack(pady=20)

    nome_entry = ctk.CTkEntry(
        main_frame,
        placeholder_text="Nome da pizzaria"
    )
    nome_entry.pack(pady=10)

    quantidade_entry = ctk.CTkEntry(
        main_frame,
        placeholder_text="Quantidade de folhas"
    )
    quantidade_entry.pack(pady=10)

    mensagem = ctk.CTkLabel(
        main_frame,
        text=""
    )
    mensagem.pack(pady=10)

    def retirar():
        estoque = carregar_estoque()
        nome = nome_entry.get().strip().title()
        quantidade = quantidade_entry.get().strip()
        if nome == "":
            mensagem.configure(
            text="Digite o nome da pizzaria"
            )
            return
        if quantidade == "":
            mensagem.configure(
            text="Digite a quantidade"
            )
            return
        try:
            quantidade = int(quantidade)
        except ValueError:
            mensagem.configure(
            text="Digite apenas números."
            )
            return
        
        if nome not in estoque:
            mensagem.configure(
                text="Pizzaria não encontrada."
            )
            return

        if quantidade > estoque[nome]:
            mensagem.configure(
                text="Estoque insuficiente"
            )
            return

        estoque[nome] -= quantidade

        salvar_estoque(estoque)

        registrar_movimentacao(
            nome,
            "Saída",
            quantidade
        )
        
        nome_entry.delete(0, "end")
        quantidade_entry.delete(0, "end")

        mensagem.configure(
            text="✅ Saída registrada com sucesso!"
        )

        mensagem.after(
            2000,
            lambda: mensagem.configure(text="")
        )
    botao_retirada = ctk.CTkButton(
        main_frame,
        text="Retirar",
        command=retirar
        )
    botao_retirada.pack(pady=20)   

def abrir_relatorios():
    limpar_tela()

    titulo = ctk.CTkLabel(
        main_frame,
        text="Relatórios",
        font=("Arial", 22, "bold")
    )
    titulo.pack(pady=20)

    relatorio_frame = ctk.CTkFrame(main_frame)

    relatorio_frame.pack(
        fill = "both",
        expand = True,
        padx = 20,
        pady = 10
    )

    estoque = carregar_estoque()
    historico = carregar_historico()
    print(historico)
    print(len(historico))

    cards_frame = ctk.CTkFrame(relatorio_frame)
    cards_frame.pack(
        fill="x",
        pady=10
    )

    card_total = ctk.CTkFrame(cards_frame)
    card_total.pack(
        side="left",
        padx=10,
        pady=10,
        expand=True,
        fill="x"
    )

    ctk.CTkLabel(
        card_total,
        text="📦 Total de folhas:",
        font=("Arial", 16, "bold")
    ).pack(pady=(10,5))
    ctk.CTkLabel(
        card_total,
        text=sum(estoque.values()),
        font=("Arial", 34, "bold")
    ).pack(pady=(0,10))

    cards_pizzarias = ctk.CTkFrame(cards_frame)
    cards_pizzarias.pack(
        side="left",
        padx=10,
        pady=10,
        expand=True,
        fill="x"
    )

    ctk.CTkLabel(
        cards_pizzarias,
        text="🏪 Total de pizzarias",
        font=("Arial", 16, "bold")
    ).pack(pady=(10,5))
    ctk.CTkLabel(
        cards_pizzarias,
        text=len(estoque),
        font=("Arial",34, "bold")
    ).pack(pady=(0,10))

    estoque_baixo_frame = ctk.CTkFrame(relatorio_frame)
    estoque_baixo_frame.pack(
        fill="x",
        padx=10,
        pady=10
    )

    ctk.CTkLabel(
        estoque_baixo_frame,
        text="⚠ Estoques baixos",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    baixo = False
    for nome, quantidade in estoque.items():
        if quantidade <=100:
            baixo = True

            ctk.CTkLabel(
                estoque_baixo_frame,
                text=f"{nome} - {quantidade} folhas"
            ).pack(anchor="w", padx=20)

    if not baixo:
        ctk.CTkLabel(
            estoque_baixo_frame,
            text="Nenhum estoque baixo"
        ).pack(pady=10)

    historico_frame = ctk.CTkScrollableFrame(
        relatorio_frame,
        height=200
    )
    historico_frame.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    ctk.CTkLabel(
        historico_frame,
        text="📜 Últimas movimentações",
        font=("Arial", 18 ,"bold")
    ).pack(pady=10)

    ultimas = historico[-10:]

    for movimentacao in reversed(ultimas):
        card = ctk.CTkFrame(
            historico_frame
        )
        card.pack(
            fill="x",
            padx=10,
            pady=5
        )
        if movimentacao["tipo"] == "Entrada":
            icone = "📥"
            cor = "white"
        else:
            icone = "📥"
            cor = "red"

        

        ctk.CTkLabel(
            card,
            text=f"{icone} {movimentacao['tipo']}",
            text_color=cor,
            font=("Arial", 18, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(10,5)
        )
        ctk.CTkLabel(
            card,
            text=f"🍕 {movimentacao['pizzaria']}",
            font=("Arial",16)
        ).pack(
            anchor="w",
            padx=15
        )
        ctk.CTkLabel(
            card,
            text=f"📦 {movimentacao['quantidade']} folhas",
            font=("Arial",16)
        ).pack(
            anchor="w",
            padx=15
        )
        ctk.CTkLabel(
            card,
            text=f"🕒 {movimentacao['data']}",
            font=("Arial", 14)
        ).pack(
            anchor="w",
            padx=15,
            pady=(0,10)
        )

def sair():
    app.destroy()




# ---------------- TÍTULO ----------------

titulo = ctk.CTkLabel(
    menu_frame,
    text="📦 StockControl",
    font=("Arial", 20)
)

titulo.pack(
    pady=20
)


# ---------------- BOTÕES ----------------

botoes = [
    "➕ Cadastrar",
    "🔍 Consultar",
    "📋 Listar Todas",
    "📥 Entrada",
    "📤 Saída",
    "📊 Relatórios",
    "🚪 Sair"
]


funcoes = {
    "➕ Cadastrar": abrir_cadastro,
    "🔍 Consultar": abrir_consulta,
    "📋 Listar Todas": abrir_listar_todas,
    "📥 Entrada": abrir_entrada,
    "📤 Saída": abrir_saida,
    "📊 Relatórios": abrir_relatorios,
    "🚪 Sair": sair
}


for nome_botao in botoes:

    botao = ctk.CTkButton(
        menu_frame,
        text=nome_botao,
        command=funcoes[nome_botao]
    )

    botao.pack(
        pady=10,
        padx=20
    )


# ---------------- EXECUTAR ----------------

app.mainloop()