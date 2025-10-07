import json

# lettura del file JSON
with open("C:\\Users\\Maboi\\OneDrive\\02_Education\\02_ProCert\\04_Formatemp\\04_Web-AI-ML\\Json\\text.Json", "r", encoding="utf-8") as f:
    studenti = json.load(f)

# Filtro i sufficienti
promossi = [studente for studente in studenti if studente["voto"] >= 6]

# Stampo i promossi
print("Studenti promossi:")
for studente in promossi:
    print(f"{studente['nome']} - {studente['voto']}")

# Salvo i promossi in un nuovo file JSON
with open("Json/promossi.json", "w", encoding="utf-8") as f:
    json.dump(promossi, f, ensure_ascii=False, indent=4)
