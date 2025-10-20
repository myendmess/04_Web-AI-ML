import json

def analizza_file_json(percorso_file):
    try:
        with open(percorso_file, "r", encoding="utf-8") as file:
            dati = json.load(file)
        print(f"\nFile '{percorso_file}' caricato correttamente.\n")
    except json.JSONDecodeError as e:
        print(f"\n❌ Errore nel file '{percorso_file}': JSON non valido.")
        print("Dettagli:", e)
        return
    except FileNotFoundError:
        print(f"\nIl file '{percorso_file}' non esiste.")
        return

    # Analisi del contenuto
    errori = []
    for i, prodotto in enumerate(dati, start=1):
        if not isinstance(prodotto, dict):
            errori.append(f"Elemento {i} non è un oggetto valido.")
            continue

        nome = prodotto.get("prodotto")
        quantita = prodotto.get("quantita")
        prezzo = prodotto.get("prezzo")

        # Controllo campi mancanti
        if nome is None or quantita is None or prezzo is None:
            errori.append(f"Elemento {i}: campi mancanti ({prodotto}).")
            continue

        # Controllo tipi
        if not isinstance(quantita, (int, float)):
            errori.append(f"Elemento {i}: 'quantita' non è numerica ({quantita}).")
        if not isinstance(prezzo, (int, float)):
            errori.append(f"Elemento {i}: 'prezzo' non è numerico ({prezzo}).")

    if errori:
        print("Il file è stato letto, ma contiene problemi nei dati:")
        for e in errori:
            print(" -", e)
    else:
        print("Tutti i dati sono coerenti e utilizzabili.")

# ESEMPIO DI USO:
analizza_file_json("17_prodotti1.json")
# analizza_file_json("17_rodotti2.json")
