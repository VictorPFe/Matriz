from customtkinter import *
from componentes.funcionalidades import Funcionalidades
from db.postgre import desconectar
from db.Schemes.esquemas import esquemas

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Gerenciamento de Matriz SoD")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        esquemas()

        self.funcionalidades = Funcionalidades(self)
        self.funcionalidades.grid(row=0, column=0, padx=20, pady=20, sticky="nws")


app = App()
app.mainloop()

try:
    desconectar()
except:
    None
