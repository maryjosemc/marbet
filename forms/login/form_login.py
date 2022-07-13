import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from forms.login.form_login_design import DiseñoFormularioLogin
import util.generic as utl
from forms.master.form_master import MasterPanel

class formularioLlogin(DiseñoFormularioLogin):


    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()
        if(usu =="root" and password == "1234"):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="La contraseña no es correcta", title="Mensaje")

    def _init_(self):
        super()._init_()  

      



