from cryptography.fernet import Fernet
# Funcion para encriptar el password, primero se transforma a valores de bites para poder guardarlos posteriormente
def encriptado (password:str):
    f = Fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NKPWTrZN5g=')
    b_password = bytes(password,'ascii')
    password_encryptada = f.encrypt(b_password)
    return password_encryptada.decode('ascii')


#pimero pasamos los datos para ser desencriptado y despues se devueve en codigo ascci
def desEncryptado (password:str):
    f = Fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NKPWTrZN5g=')
    b_password = bytes(password,'ascii')
    b_password_desencyptada = f.decrypt(b_password)
    return b_password_desencyptada.decode('ascii')
