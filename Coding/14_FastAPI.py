from fastapi import FastAPI, HTTPException

app = FastAPI()

# Dizionario: chiave = id utente
utenti = {
    1: {"nome": "Alice", "email": "alice@gmail.com"},
    2: {"nome": "Bob", "email": "bob@gmail.com"},
    3: {"nome": "Charlie", "email": "charlie@gmail.com"}
}

@app.get("/utenti/{user_id}")
def get_utente(user_id: int):
    if user_id in utenti:
        return utenti[user_id]
    else:
        # se non esiste l'utente ritorna un errore 404
        raise HTTPException(status_code=404, detail="Utente non trovato")
print("Server FastAPI in esecuzione su http://localhost:8000")