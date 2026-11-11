from pydantic import BaseModel
from typing import Optional


class EmpresaCreate(BaseModel):
    nome_empresa: str
    responsavel: str
    cnpj: str
    email: str
    telefone: Optional[str] = None
    whatsapp: Optional[str] = None
    foto_perfil: Optional[str] = None
    estado: str
    regiao: str
    cidade: str


class EmpresaResponse(EmpresaCreate):
    id: int

    class Config:
        from_attributes = True