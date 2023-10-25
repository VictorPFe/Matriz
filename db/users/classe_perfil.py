from customtkinter import *
from db.users.CRUD.criar_perfil import novoUsuario

class JanelaUsuario(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Usuario")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.ajuste = oPerfil(self)
        self.ajuste.grid(row=0, column=0, padx=20, pady=20)

        # Adicione o bind para a tecla Enter
        self.bind("<Return>", self.obter)

    def obter(self, event=None):  # Adicione o argumento 'event' com valor padrão None
        nome_do_perfil = self.ajuste.nome_do_perfil.get()
        senha = self.ajuste.senha.get()
        descricao_do_usuario = self.ajuste.descricao_do_usuario.get()
        cpf = self.ajuste.cpf.get()
        codigo_sistema = self.ajuste.codigo_sistema.get()

        novoUsuario(nome_do_perfil, descricao_do_usuario, senha, cpf, codigo_sistema)

        # Feche a janela corretamente
        self.destroy()

class oPerfil(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.legenda_cadastros = CTkLabel(self, text="Cadastrar Usuário", font=("sans-serif", 18))
        self.legenda_cadastros.grid(row=0, column=0, padx=30, pady=(60, 0))

        self.nome_do_perfil = CTkEntry(self, placeholder_text="Id de Usuario")
        self.nome_do_perfil.grid(row=1, column=0, padx=20, pady=(20, 15))

        self.senha = CTkEntry(self, placeholder_text="Senha")
        self.senha.grid(row=2, column=0, padx=20, pady=(15, 10))

        self.cpf = CTkEntry(self, placeholder_text="CPF")
        self.cpf.grid(row=3, column=0, padx=20, pady=(15, 10))

        self.codigo_sistema = CTkEntry(self, placeholder_text="Codigo Sistema")
        self.codigo_sistema.grid(row=4, column=0, padx=20, pady=(15, 10))

        self.descricao_do_usuario = CTkEntry(self, placeholder_text="Descrição de Usuário")
        self.descricao_do_usuario.grid(row=6, column=0, padx=20, pady=(15, 10))

        self.salvar = CTkButton(self, text="Cadastrar", command=lambda: self.master.obter())
        self.salvar.grid(row=7, column=0, padx=20, pady=20)
