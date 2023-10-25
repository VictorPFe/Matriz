from psycopg2 import *
from customtkinter import *
from db.postgre import conectar_banco_dados
from db.users.CRUD.deletar_perfil import deletarUsuario
from db.users.CRUD.editar_perfil import EditarUsuario

class fetchUsuarios(CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.carregar_registros()

    def carregar_registros(self):
        conn = conectar_banco_dados()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM perfis_de_acesso")

        registros = cursor.fetchall()

        row_num = 0

        for registro in registros:
            id, nome_do_perfil, descricao_do_usuario, codigo_sistema, senha, cpf, adm = registro

            self.display_fetching = perfil(self, id, nome_do_perfil, descricao_do_usuario, codigo_sistema, senha, cpf, adm, self.atualizar, self.editar)
            self.display_fetching.grid(row=row_num, column=0, padx=20, pady=(15, 0), sticky="ew")
            self.display_fetching.configure(fg_color="#444")

            row_num += 1

        cursor.close()
        conn.close()

    def atualizar(self):
        # Limpe os widgets existentes
        for widget in self.grid_slaves():
            widget.grid_remove()

        # Recarregue os registros
        self.carregar_registros()

    def editar(self, id, nome_do_perfil, descricao_do_usuario, codigo_sistema, senha, cpf):
        EditarUsuario(self, id, nome_do_perfil, descricao_do_usuario, codigo_sistema, senha, cpf)

class perfil(CTkFrame):
    def __init__(self, parent, id, nome_do_perfil, descricao_do_usuario, codigo_sistema, senha, cpf, adm, atualizar, editar):
        super().__init__(parent)

        # Pra criar um deletar, pega "codigo" e usa como id pra deletar o item
        self.excluir = CTkButton(self, text="Excluir", command=lambda: (deletarUsuario(id, nome_do_perfil, descricao_do_usuario, codigo_sistema, senha, cpf, adm), atualizar()))
        self.excluir.grid(row=0, column=0, padx=(20, 5), pady=10)
        self.excluir.configure(width=50)

        self.edit = CTkButton(self, text="Editar", command=lambda: editar(nome_do_perfil, descricao_do_usuario, senha))
        self.edit.grid(row=0, column=1, padx=(5, 20), pady=10)
        self.edit.configure(width=50)

        self.nome_do_perfil = CTkLabel(self, text=nome_do_perfil, font=("Roboto", 15))
        self.nome_do_perfil.grid(row=0, column=2, padx=5, pady=10)

        self.descricao_do_usuario = CTkLabel(self, text=descricao_do_usuario, font=("Roboto", 15))
        self.descricao_do_usuario.grid(row=0, column=3, padx=5, pady=10)

        self.senha = CTkLabel(self, text=senha, font=("Roboto", 15))
        self.senha.grid(row=0, column=4, padx=5, pady=10)