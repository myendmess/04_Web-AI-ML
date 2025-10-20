from pathlib import Path

# 1️⃣ Definire la cartella logs
logs_folder = Path("logs")
logs_folder.mkdir(exist_ok=True)

# 2️⃣ Creare alcuni file di esempio con righe normali ed errori
sample_logs = {
    "log1.txt": [
        "Avvio del sistema",
        "Errore: connessione fallita",
        "Operazione completata con successo",
        "Errore: file non trovato"
    ],
    "log2.txt": [
        "Login utente",
        "Operazione completata",
        "Attenzione: memoria bassa",
        "Errore: timeout"
    ],
    "log3.txt": [
        "Controllo aggiornamenti",
        "Aggiornamento completato",
        "Errore: accesso negato"
    ]
}

for filename, lines in sample_logs.items():
    file_path = logs_folder / filename
    with file_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines))

print("File di esempio creati con successo nella cartella 'logs'.")

# 3️⃣ Inizializzare il contatore delle righe con "errore"
error_count = 0

# 4️⃣ Scorrere tutti i file .txt nella cartella
for txt_file in logs_folder.glob("*.txt"):
    with txt_file.open("r", encoding="utf-8") as f:
        for line in f:
            if "errore" in line.lower():  # ignora maiuscole/minuscole
                error_count += 1

# 5️⃣ Salvare il risultato in un file di riepilogo
summary_file = logs_folder / "riepilogo.txt"
with summary_file.open("w", encoding="utf-8") as f:
    f.write(f"Righe contenenti 'errore': {error_count}\n")

print(f"Analisi completata! Totale righe con 'errore': {error_count}")
print(f"Risultato salvato in {summary_file}")
