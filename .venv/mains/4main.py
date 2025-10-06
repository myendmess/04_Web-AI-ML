from fastapi import FastAPI

app = FastAPI()

vendite = [
    {"cliente": "Luca", "prodotto": "mela", "quantita": 3},
    {"cliente": "Anna", "prodotto": "banana", "quantita": 5},
    {"cliente": "Luca", "prodotto": "banana", "quantita": 2},
    {"cliente": "Marco", "prodotto": "mela", "quantita": 1},
    {"cliente": "Anna", "prodotto": "mela", "quantita": 4}
]

@app.get("/stats")
def get_stats():
    # 1. Conteggio totale per prodotto
    totale_per_prodotto = {}
    for vendita in vendite:
        prodotto = vendita["prodotto"]
        quantita = vendita["quantita"]
        if prodotto in totale_per_prodotto:
            totale_per_prodotto[prodotto] += quantita
        else:
            totale_per_prodotto[prodotto] = quantita

    # 2. Totale acquistato per cliente
    totale_per_cliente = {}
    for vendita in vendite:
        cliente = vendita["cliente"]
        quantita = vendita["quantita"]
        if cliente in totale_per_cliente:
            totale_per_cliente[cliente] += quantita
        else:
            totale_per_cliente[cliente] = quantita

    # 3. Cliente che ha acquistato di più
    cliente_max = max(totale_per_cliente, key=totale_per_cliente.get) if totale_per_cliente else None

    return {
        "totale_per_prodotto": totale_per_prodotto,
        "totale_per_cliente": totale_per_cliente,
        "cliente_piu_acquistatore": cliente_max
    }
