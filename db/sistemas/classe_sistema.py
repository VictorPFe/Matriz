from customtkinter import *
from db.sistemas.CRUD.criar_sistema import novoSistema

class JanelaSistema(CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Sistemas")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.ajuste = frame(self)
        self.ajuste.grid(row=0, column=0, padx=20, pady=20)

        # Adicione o bind para a tecla Enter
        self.bind("<Return>", self.obter)

    def obter(self, event=None):  # Adicione o argumento 'event' com valor padrão None
        codigo = self.ajuste.codigo.get()
        nome_do_sistema = self.ajuste.nome.get()
        novoSistema(codigo, nome_do_sistema)
        
        # Feche a janela corretamente
        self.destroy()

class frame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.legenda_cadastros = CTkLabel(self, text="Cadastrar Sistema", font=("sans-serif", 18))
        self.legenda_cadastros.grid(row=0, column=0, padx=30, pady=(60, 0))

        self.codigo = CTkEntry(self, placeholder_text="Código do Sistema")
        self.codigo.grid(row=2, column=0, padx=20, pady=(20, 15))

        self.nome = CTkEntry(self, placeholder_text="Nome do Sistema")
        self.nome.grid(row=1, column=0, padx=20, pady=(15, 10))

        self.salvar = CTkButton(self, text="Salvar", command=lambda: self.master.obter())
        self.salvar.grid(row=3, column=0, padx=20, pady=20)
