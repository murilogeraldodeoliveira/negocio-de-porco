

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import engine, SessionLocal
from . import models, schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Negócio de Porco",
    description="Plataforma para conectar empresários por estado, região e cidade",
    version="1.0.0"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def inicio():
    return {
        "mensagem": "Negócio de Porco funcionando!"
    }


@app.post("/empresas", response_model=schemas.EmpresaResponse)
def cadastrar_empresa(
    empresa: schemas.EmpresaCreate,
    db: Session = Depends(get_db)
):
    empresa_existente = db.query(models.Empresa).filter(
        models.Empresa.cnpj == empresa.cnpj
    ).first()

    if empresa_existente:
        raise HTTPException(
            status_code=400,
            detail="Já existe uma empresa cadastrada com este CNPJ."
        )

    nova_empresa = models.Empresa(**empresa.model_dump())

    db.add(nova_empresa)
    db.commit()
    db.refresh(nova_empresa)

    return nova_empresa

@app.get("/empresas", response_model=list[schemas.EmpresaResponse])
def listar_empresas(db: Session = Depends(get_db)):
    empresas = db.query(models.Empresa).all()
    return empresas

@app.get("/empresas/{empresa_id}", response_model=schemas.EmpresaResponse)
def buscar_empresa(empresa_id: int, db: Session = Depends(get_db)):
    empresa = db.query(models.Empresa).filter(
        models.Empresa.id == empresa_id
    ).first()

    if not empresa:
        raise HTTPException(
            status_code=404,
            detail="Empresa não encontrada."
        )

    return empresa

@app.delete("/empresas/{empresa_id}")
def excluir_empresa(empresa_id: int, db: Session = Depends(get_db)):
    empresa = db.query(models.Empresa).filter(
        models.Empresa.id == empresa_id
    ).first()

    if not empresa:
        raise HTTPException(
            status_code=404,
            detail="Empresa não encontrada."
        )

    db.delete(empresa)
    db.commit()

    return {
        "mensagem": "Empresa excluída com sucesso."
    }

@app.put("/empresas/{empresa_id}", response_model=schemas.EmpresaResponse)
def editar_empresa(
    empresa_id: int,
    dados: schemas.EmpresaCreate,
    db: Session = Depends(get_db)
):
    empresa = db.query(models.Empresa).filter(
        models.Empresa.id == empresa_id
    ).first()

    if not empresa:
        raise HTTPException(
            status_code=404,
            detail="Empresa não encontrada."
        )

    cnpj_em_uso = db.query(models.Empresa).filter(
        models.Empresa.cnpj == dados.cnpj,
        models.Empresa.id != empresa_id
    ).first()

    if cnpj_em_uso:
        raise HTTPException(
            status_code=400,
            detail="Este CNPJ já pertence a outra empresa."
        )

    for campo, valor in dados.model_dump().items():
        setattr(empresa, campo, valor)

    db.commit()
    db.refresh(empresa)

    return empresa