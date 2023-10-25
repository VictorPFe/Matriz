from customtkinter import *
from db.users.classe_perfil import JanelaUsuario
from db.users.CRUD.fetch_perfis import fetchUsuarios
from db.sistemas.classe_sistema import JanelaSistema
from db.sistemas.CRUD.fetch_sistemas import fetchSistemas


class User(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Usuários")
        self.geometry("500x300")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame = Perfil(self, self.abrirUsuarios(), self.reload)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nwe")

        self.fetch = fetchUsuarios(self)
        self.fetch.grid(row=1, column=0, padx=20, pady=20, sticky="nwes")

    def abrirUsuarios(self):
        JanelaUsuario(self)

    def reload(self):
        self.fetch.atualizar()

class Perfil(CTkFrame):
    def __init__(self, parent, executar, atualizar):
        super().__init__(parent)

        self.create = CTkButton(self, text="Cadastrar Usuario", corner_radius=8, command=executar)
        self.create.grid(row=0, column=0, padx=(20, 15), pady=(21, 20), sticky="e")
        self.create.configure(width=27, height=27)

        self.search = CTkEntry(self, placeholder_text="Buscar")
        self.search.grid(row=0, column=1, padx=(0, 15), pady=20, sticky="e")

        self.search = CTkEntry(self, placeholder_text="Codigo Sistema")
        self.search.grid(row=0, column=1, padx=(0, 15), pady=20, sticky="e")

        self.btn_search = CTkButton(self, text="?", corner_radius=8)
        self.btn_search.grid(row=0, column=2, padx=(0, 15), pady=(21, 20), sticky="e")
        self.btn_search.configure(width=27, height=27)

        self.reload = CTkButton(self, text="Atualizar", corner_radius=8, command=atualizar)
        self.reload.grid(row=0, column=3, padx=0, pady=(21, 20), sticky="e")
        self.reload.configure(width=27, height=27)


class Systems(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Sistemas")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.frame = OFrame(self, self.abrirSistemas, self.reload)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nwe")

        self.fetch = fetchSistemas(self)
        self.fetch.grid(row=1, column=0, padx=20, pady=20, sticky="nwes")

    def abrirSistemas(self):
        JanelaSistema(self)

    def reload(self):
        self.fetch.atualizar()


class OFrame(CTkFrame):
    def __init__(self, parent, executar, atualizar):
        super().__init__(parent)

        self.create = CTkButton(self, text="Cadastrar Sistema", corner_radius=8, command=executar)
        self.create.grid(row=0, column=0, padx=(20, 15), pady=(21, 20), sticky="e")
        self.create.configure(width=27, height=27)

        self.search = CTkEntry(self, placeholder_text="Buscar")
        self.search.grid(row=0, column=1, padx=(0, 15), pady=20, sticky="e")

        self.btn_search = CTkButton(self, text="Buscar", corner_radius=8)
        self.btn_search.grid(row=0, column=2, padx=(0, 15), pady=(21, 20), sticky="e")
        self.btn_search.configure(width=27, height=27)

        self.reload = CTkButton(self, text="F5", corner_radius=8, command=atualizar)
        self.reload.grid(row=0, column=3, padx=0, pady=(21, 20), sticky="e")
        self.reload.configure(width=27, height=27)
