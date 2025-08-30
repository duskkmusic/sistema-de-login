import customtkinter as ctk

ctk.set_appearance_mode("dark")

# Janela principal de login
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("300x300") 

# Labels e entradas
ctk.CTkLabel(app, text="Usuário:").pack(pady=(20,5))
entrada_usuario = ctk.CTkEntry(app)
entrada_usuario.pack(pady=5)

ctk.CTkLabel(app, text="Senha:").pack(pady=(10,5))
entrada_senha = ctk.CTkEntry(app, show="*")
entrada_senha.pack(pady=5)

mensagem = ctk.CTkLabel(app, text="")
mensagem.pack(pady=10)

# Função para abrir o painel principal
def abrir_painel():
    painel = ctk.CTk()  # cria nova janela
    painel.title("Painel do Usuário")
    painel.geometry("400x300")
    ctk.CTkLabel(painel, text="Bem-vindo, admin!", font=("Arial", 18)).pack(pady=50)
    painel.mainloop()  # mantém o painel aberto

# Função de verificação
def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if usuario == "admin" and senha == "1234":
        mensagem.configure(text="Login bem-sucedido!", text_color="green")
        app.destroy()   # fecha a janela de login
        abrir_painel()  # abre o painel
    else:
        mensagem.configure(text="Usuário ou senha incorretos", text_color="red")

# Botão de login
ctk.CTkButton(app, text="Entrar", command=verificar_login).pack(pady=20)

app.mainloop()
