from PIL import ImageTk, Image

def leer_imagen(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))

def centrar_ventana(ventana,aplication_ancho,aplication_largo):
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int ((pantall_ancho/2) - (aplication_ancho/2))
    y = int((pantall_largo/2) - (aplication_largo/2))
    return ventana.geometry(f"{aplication_ancho}x{aplication_largo}+{x}+{y}") 