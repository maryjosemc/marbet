import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from forms.login.form_login_design import Dise├▒oFormularioLogin
import util.generic as utl
from forms.master.form_master import MasterPanel

class formularioLlogin(Dise├▒oFormularioLogin):


    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()
        if(usu =="root" and password == "1234"):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="La contrase├▒a no es correcta", title="Mensaje")

    def _init_(self):
        super()._init_()  

      



