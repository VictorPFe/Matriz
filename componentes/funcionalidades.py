from customtkinter import *
from componentes.func_btns import *


class Funcionalidades(CTkFrame):
   def __init__(self, master):
      super().__init__(master)

      # sticky é aonde o conteudo vai "grudar", as posições são north, south, west, east
      # exemplo: sticky="nsw" (significa => cima, baixo e esquerda)
      self.legenda_login = CTkLabel(self, text="Login", font=("sans-serif", 18))
      self.legenda_login.grid(row=0, column=0, padx=30, pady=(30, 0))

      self.user = CTkEntry(self, placeholder_text="Id de Usuário")
      self.user.grid(row=1, column=0, padx=30, pady=10, sticky="w")

      self.senha = CTkEntry(self, placeholder_text="Senha", show="*")
      self.senha.grid(row=2, column=0, padx=30, pady=10, sticky="w")

      self.cpf = CTkEntry(self, placeholder_text="CPF")
      self.cpf.grid(row=3, column=0, padx=30, pady=10, sticky="w")

      self.confirmar = CTkButton(self, text="Entrar")
      self.confirmar.grid(row=4, column=0, padx=30, pady=10, sticky="w")

      # Divisória

      self.legenda_cadastros = CTkLabel(self, text="Cadastros", font=("sans-serif", 18))
      self.legenda_cadastros.grid(row=5, column=0, padx=30, pady=(60, 0))

      self.users = CTkButton(self, text="Usuários", command=self.user_window)
      self.users.grid(row=6, column=0, padx=30, pady=(25, 0), sticky="w")

      self.systems = CTkButton(self, text="Sistemas", command=self.sys_window)
      self.systems.grid(row=7, column=0, padx=30, pady=(25, 0), sticky="w")

      self.matriz = CTkButton(self, text="Matriz")
      self.matriz.grid(row=8, column=0, padx=30, pady=(25, 20), sticky="w")

   def user_window(self):
      User(self.master)

   def sys_window(self):
      Systems(self)