from fastapi import FastAPI
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Trello Clone API",
    description="API REST para gestión de tableros y tareas",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
