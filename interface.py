import customtkinter as ctk
import json

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
    print("Tela de consulta")


def abrir_entrada():
    print("Tela de entrada de folhas")


def abrir_saida():
    print("Tela de saída de folhas")


def abrir_relatorios():
    print("Tela de relatórios")


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
    "📥 Entrada",
    "📤 Saída",
    "📊 Relatórios",
    "🚪 Sair"
]


funcoes = {
    "➕ Cadastrar": abrir_cadastro,
    "🔍 Consultar": abrir_consulta,
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