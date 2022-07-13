import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl


class DiseñoFormularioLogin:


    def verificar(self):
        pass

    def registroUsuario(self):
        pass




     #  usu = self.usuario.get()
     #  password = self.password.get()
     #  if(usu =="root" and password == "1234"):
     #      self.ventana.destroy()
     #      MasterPanel()
     #  else:
     #      messagebox.showerror(message="La contraseña no es correcta", title="Mensaje")





    def __init__(self):
         self.ventana = tk.Tk()
         self.ventana.title('Inicio de sesion')
         self.ventana.geometry('800x500')
         self.ventana.config(bg='#fcfcfc')
         self.ventana.resizable(width=0,height=0)
         utl.centrar_ventana(self.ventana,800,500)
         

        
         logo =utl.leer_imagen("./Imagen/logo.jpg", (300, 300))
        
         #Frame del logo
         #cuadro izquierdo de la ventana donde esta el logo
         frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#014586') 
         frame_logo.pack(side="left",expand=tk.NO,fill=tk.BOTH)
         label = tk.Label(frame_logo, image=logo,bg='#014586')
         label.place(x=0,y=0,relwidth=1,relheight=1)
         #Frame del logo
         

         #frame_form
         #Cuadro derecho de color blanco
         frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
         frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
         #frame_form
         

         #frame_form_top
         #Encabezado del login Sistema de consulta
         frame_form_top = tk.Frame(frame_form,height = 90, bd=0, relief=tk.SOLID, bg='black')
         frame_form_top.pack(side="top", fill = tk.X)
         title = tk.Label(frame_form_top, text="SISTEMA DE CONSULTA", font=('Times', 30), fg="#666a88", bg='#fcfcfc', pady=20)
         title.pack(expand=tk.YES,fill=tk.BOTH)
         #frame_for_top

        #frame_form_top
         #Encabezado 2 Inicio de sesion
         frame_form_top2 = tk.Frame(frame_form,height = 10, bd=0, relief=tk.SOLID, bg='black')
         frame_form_top2.pack(side="top", fill = tk.X)
         title = tk.Label(frame_form_top2, text="INICIO DE SESION", font=('Times', 20), fg="#666a88", bg='#fcfcfc', pady=30)
         title.pack(expand=tk.YES,fill=tk.BOTH)
         #frame_for_top

         #Frame de rellenado
         frame_form_fill = tk.Frame(frame_form,height = 40, bd=0, relief=tk.SOLID,bg='#fcfcfc')
         frame_form_fill.pack(side="bottom", expand=tk.YES,fill=tk.BOTH)


         etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14), fg="#666a88", bg='#fcfcfc',anchor="w")
         etiqueta_usuario.pack(fill=tk.X,padx=20,pady=5)
         self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
         self.usuario.pack(fill=tk.X,padx=20,pady=10)


         etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc',anchor="w")
         etiqueta_password.pack(fill=tk.X,padx=20,pady=5)
         self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
         self.password.pack(fill=tk.X,padx=20,pady=10)
         self.password.config(show="*")

        #Boton de inicio de sesion
         inicio= tk.Button(frame_form_fill,text="Iniciar sesion", font=('Times', 15,BOLD), bg='#3a7ff6', bd =0,fg="#fff",command=self.verificar)
         inicio.pack(fill=tk.X, padx=20,pady=20)
         inicio.bind("<Return>", (lambda event: self.verificar()))  


        #Boton de registro
         inicio= tk.Button(frame_form_fill,text="Registrar usuario", font=('Times', 15), bg='#fcfcfc', bd =0,fg="#3a7ff6",command=self.registroUsuario)
         inicio.pack(fill=tk.X, padx=20,pady=20)
         inicio.bind("<Return>", (lambda event: self.registroUsuario()))  

         #Frame de rellenado


         self.ventana.mainloop()


