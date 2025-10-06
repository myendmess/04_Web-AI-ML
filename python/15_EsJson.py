
# "Rotta" per cancellare un utente
import json

# Dizionario utenti
users = {
    1: {"nome": "cristian", "cognome": "chirivi"},
    2: {"nome": "carlo", "cognome": "mazzotta"},
    3: {"nome": "peppe", "cognome": "esposito"}
}

# "Rotta" per cancellare un utente
def delete_user(user_id: int):
    print(f"param {user_id}")
    if user_id in users:
        del users[user_id]
        return users
    else:
        return {"error": "Utente non trovato"}

# "Rotta" per modificare un utente
def put_user(user_id: int, nome: str, cognome: str):
    if user_id in users:
        users[user_id] = {"nome": nome, "cognome": cognome}
        return users[user_id]
    else:
        return {"error": "Utente non trovato"}

# Test con json.dumps per stampe più leggibili
print(json.dumps(delete_user(1), indent=2, ensure_ascii=False))   # elimina l'utente con id 1
print(json.dumps(users, indent=2, ensure_ascii=False))            # mostra il nuovo dizionario

print(json.dumps(put_user(2, "Gianni", "Rossi"), indent=2, ensure_ascii=False))  # modifica utente con id 2
print(json.dumps(users, indent=2, ensure_ascii=False))
