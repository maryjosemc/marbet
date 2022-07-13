import sqlalchemy as db 
from persistence.modelos import Auth_Usuario
from sqlalchemy.orm import Session

class AutUsarioRepositorio():
    def _init_(self):
        self.engine = db.creae_engine('sqlite:///db/login.sqlite',echo=False,future=False)


    def obtenerUsuarioNombre(self, user_name: str):
        user: Auth_Usuario = None
        with Session(self.engine) as session:
            user= session.query(Auth_Usuario).filter_by(
                username=user_name).first()
        return user

    def insertarUsurio(self, user: Auth_Usuario):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()
            
                

