# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Dati di partenza
studenti = [
    {"nome": "Alice", "voti": [28, 30, 25]},
    {"nome": "Bruno", "voti": [15, 20, 17]},
    {"nome": "Carla", "voti": [30, 30, 29]},
]

# Modello di risposta
class Studente(BaseModel):
    nome: str
    media: float

@app.get("/promossi", response_model=List[Studente])
def get_promossi():
    """
    Restituisce la lista degli studenti con media >= 18
    """
    promossi = []
    for s in studenti:
        media = sum(s["voti"]) / len(s["voti"])
        if media >= 18:
            promossi.append({"nome": s["nome"], "media": round(media, 2)})
    return promossi
