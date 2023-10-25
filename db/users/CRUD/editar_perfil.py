from psycopg2 import *
from db.postgre import conectar_banco_dados
from customtkinter import *


class EditarUsuario(CTkToplevel):
    def __init__(self, parent, nome_do_perfil, descricao_do_usuario, senha):
        super().__init__(parent)

        self.title("Usuarios")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.ajuste = frame(self, nome_do_perfil, descricao_do_usuario, senha)
        self.ajuste.grid(row=0, column=0, padx=20, pady=20)

        # Adicione o bind para a tecla Enter
        self.bind("<Return>", self.update)

    def update(self, event=None):  # Adicione o argumento 'event' com valor padrão None
        senha = self.ajuste.name.get()
        nome_do_perfil = self.ajuste.name.get()
        descricao_do_usuario = self.ajuste.name.get()
        atualizar(nome_do_perfil, descricao_do_usuario, senha)

        # Feche a janela corretamente
        self.destroy()


class frame(CTkFrame):
    def __init__(self, parent, nome_do_perfil, descricao_do_usuario, senha):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.nome_do_perfil = CTkEntry(self, placeholder_text="Nome de Usuario")
        self.nome_do_perfil.grid(row=0, column=0, padx=20, pady=(20, 15))
        self.nome_do_perfil.insert(0, nome_do_perfil)  # Insira o valor inicial no campo

        self.senha = CTkEntry(self, placeholder_text="Senha")
        self.senha.grid(row=1, column=0, padx=20, pady=(15, 10))
        self.senha.insert(0, senha)  # Insira o valor inicial no campo

        self.descricao_do_usuario = CTkEntry(self, placeholder_text="Descrição do Usuario")
        self.descricao_do_usuario.grid(row=1, column=0, padx=20, pady=(15, 10))
        self.descricao_do_usuario.insert(0, descricao_do_usuario)  # Insira o valor inicial no campo

        self.salvar = CTkButton(self, text="Salvar", command=lambda: self.master.update())
        self.salvar.grid(row=2, column=0, padx=20, pady=20)


def atualizar(senha, nome_do_perfil, descricao_do_usuario):
    try:
        conn = conectar_banco_dados()
        cursor = conn.cursor()

        # Crie a instrução SQL de atualização
        sql = "UPDATE sistemas SET nome_do_perfil = %s WHERE senha = %s = %s WHERE descricao_do_usuario = %s"

        # Execute a instrução SQL com os valores desejados
        cursor.execute(sql, (nome_do_perfil, senha, descricao_do_usuario))

        # Faça o commit da transação para salvar as mudanças no banco de dados
        conn.commit()

        # Feche o cursor e a conexão
        cursor.close()
        conn.close()
    except (ValueError, Error) as e:
        print(f"Erro ao atualizar o sistema: {e}")

