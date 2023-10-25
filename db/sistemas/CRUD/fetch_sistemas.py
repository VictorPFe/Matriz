from psycopg2 import *
from customtkinter import *
from db.postgre import conectar_banco_dados
from db.sistemas.CRUD.deletar_sistema import deletarSistema
from db.sistemas.CRUD.editar_sistema import EditarSistema

class fetchSistemas(CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.carregar_registros()

    def carregar_registros(self):
        conn = conectar_banco_dados()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM sistemas")

        registros = cursor.fetchall()

        row_num = 0

        for registro in registros:
            codigo, nome_do_sistema = registro

            self.display_fetching = frame(self, codigo, nome_do_sistema, self.atualizar, self.editar)
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

    def editar(self, codigo, nome_do_sistema):
        EditarSistema(self, codigo, nome_do_sistema)

class frame(CTkFrame):
   def __init__(self, parent, codigo, nome_do_sistema, atualizar, editar):
      super().__init__(parent)

      # Pra criar um deletar, pega "codigo" e usa como id pra deletar o item
      self.excluir = CTkButton(self, text="Excluir", command=lambda: (deletarSistema(codigo), atualizar()))
      self.excluir.grid(row=0, column=0, padx=(20, 5), pady=10)
      self.excluir.configure(width=50)


      self.edit = CTkButton(self, text="Editar", command=lambda: editar(codigo, nome_do_sistema))
      self.edit.grid(row=0, column=1, padx=(5, 20), pady=10)
      self.edit.configure(width=50)

      self.id = CTkLabel(self, text=codigo, font=("Roboto", 15))
      self.id.grid(row=0, column=2, padx=(10, 0), pady=10)

      self.nome = CTkLabel(self, text=nome_do_sistema, font=("Roboto", 15))
      self.nome.grid(row=0, column=3, padx=5, pady=10)
