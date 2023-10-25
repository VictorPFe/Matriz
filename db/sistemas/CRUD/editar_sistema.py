from psycopg2 import *
from db.postgre import conectar_banco_dados
from customtkinter import *

class EditarSistema(CTkToplevel):
    def __init__(self, parent, codigo, nome_do_sistema):
        super().__init__(parent)

        self.title("Sistemas")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.ajuste = frame(self, codigo, nome_do_sistema)
        self.ajuste.grid(row=0, column=0, padx=20, pady=20)

        # Adicione o bind para a tecla Enter
        self.bind("<Return>", self.update)

    def update(self, event=None):  # Adicione o argumento 'event' com valor padrão None
        codigo = self.ajuste.codigo.get()
        nome_do_sistema = self.ajuste.nome.get()
        atualizar(codigo, nome_do_sistema)
        
        # Feche a janela corretamente
        self.destroy()

class frame(CTkFrame):
    def __init__(self, parent, codigo, nome_do_sistema):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.codigo = CTkEntry(self, placeholder_text="Código do Sistema")
        self.codigo.grid(row=0, column=0, padx=20, pady=(20, 15))
        self.codigo.insert(0, codigo)  # Insira o valor inicial no campo

        self.nome = CTkEntry(self, placeholder_text="Nome do Sistema")
        self.nome.grid(row=1, column=0, padx=20, pady=(15, 10))
        self.nome.insert(0, nome_do_sistema)  # Insira o valor inicial no campo


        self.salvar = CTkButton(self, text="Salvar", command=lambda: self.master.update())
        self.salvar.grid(row=2, column=0, padx=20, pady=20)

def atualizar(codigo, sistema):
    try:
        conn = conectar_banco_dados()
        cursor = conn.cursor()


        # Crie a instrução SQL de atualização
        sql = "UPDATE sistemas SET nome_do_sistema = %s WHERE codigo = %s"

        # Execute a instrução SQL com os valores desejados
        cursor.execute(sql, (sistema, codigo))

        # Faça o commit da transação para salvar as mudanças no banco de dados
        conn.commit()

        # Feche o cursor e a conexão
        cursor.close()
        conn.close()
    except (ValueError, Error) as e:
        print(f"Erro ao atualizar o sistema: {e}")

