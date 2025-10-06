
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

vendite = [
    {"cliente": "Luca", "prodotto": "mela", "quantita": 3},
    {"cliente": "Anna", "prodotto": "banana", "quantita": 5},
    {"cliente": "Luca", "prodotto": "banana", "quantita": 2},
    {"cliente": "Marco", "prodotto": "mela", "quantita": 1},
    {"cliente": "Anna", "prodotto": "mela", "quantita": 4},
]

@app.get("/stats")
def get_stats(
    cliente: Optional[str] = Query(None, description="Nome del cliente da filtrare"),
    prodotto: Optional[str] = Query(None, description="Nome del prodotto da filtrare")
):
    # Filtra vendite in base ai parametri
    vendite_filtrate = vendite
    if cliente:
        vendite_filtrate = [v for v in vendite_filtrate if v["cliente"].lower() == cliente.lower()]
    if prodotto:
        vendite_filtrate = [v for v in vendite_filtrate if v["prodotto"].lower() == prodotto.lower()]

    if not vendite_filtrate:
        return {"messaggio": "Nessun dato trovato con i filtri applicati"}

    # Conteggio prodotti
    prodotti_count = {}
    for v in vendite_filtrate:
        prodotti_count[v["prodotto"]] = prodotti_count.get(v["prodotto"], 0) + v["quantita"]

    # Totale per cliente
    clienti_totali = {}
    for v in vendite_filtrate:
        clienti_totali[v["cliente"]] = clienti_totali.get(v["cliente"], 0) + v["quantita"]

    # Cliente top
    cliente_top = max(clienti_totali, key=clienti_totali.get)
    top_cliente = {"nome": cliente_top, "quantita": clienti_totali[cliente_top]}

    return {
        "vendite_per_prodotto": prodotti_count,
        "totale_per_cliente": clienti_totali,
        "top_cliente": top_cliente,
    }

#stats:
#http://127.0.0.1:8000/stats

#Solo per cliente = Anna:
#http://127.0.0.1:8000/stats?cliente=Anna

#Solo per prodotto = mela:
#http://127.0.0.1:8000/stats?prodotto=mela

#Per cliente = Anna e prodotto = mela:
#http://127.0.0.1:8000/stats?cliente=Anna&prodotto=mela
