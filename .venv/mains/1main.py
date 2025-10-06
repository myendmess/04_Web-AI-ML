# main.py
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List

app = FastAPI()

utenti = [
    {"nome": "Alice", "eta": 25},
    {"nome": "Bruno", "eta": 30},
    {"nome": "Carla", "eta": 22},
]

# Model per la risposta
class Utente(BaseModel):
    nome: str
    eta: int

@app.get("/utente", response_model=Utente)
def get_utente(nome: str = Query(..., description="Nome dell'utente da cercare")):
    """
    Cerca nella lista `utenti` l'oggetto con campo 'nome' uguale al query param `nome`.
    La ricerca è case-insensitive e rimuove gli spazi esterni.
    """
    cerca = nome.strip().lower()
    for u in utenti:
        if u["nome"].lower() == cerca:
            return u
    raise HTTPException(status_code=404, detail=f"Utente con nome '{nome}' non trovato")

# (Opzionale) rotta per vedere tutti gli utenti
@app.get("/utenti", response_model=List[Utente])
def list_utenti():
    return utenti
