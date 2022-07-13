from sqlalchemy import Column
from sqlalchemy import String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Auth_Usuario(Base):
    _tablaname_ ="auth_user"
    id = Column(Integer, primary_key=True, autoincrement=True)
     
    username = Column(String(150))
    password = Column(String(128))


 # def _repr_(self):
 #     return f'auth_user({self.username}), {self.password})'

 # def _str_(self):
 #     return self.username