from sqlalchemy import Column, Integer, String
from .database import Base


class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)

    nome_empresa = Column(String, nullable=False)
    responsavel = Column(String, nullable=False)
    cnpj = Column(String, unique=True, index=True, nullable=False)

    email = Column(String, unique=True, index=True, nullable=False)
    telefone = Column(String)
    whatsapp = Column(String)
    foto_perfil = Column(String, nullable=True)

    estado = Column(String, nullable=False)
    regiao = Column(String, nullable=False)
    cidade = Column(String, nullable=False)