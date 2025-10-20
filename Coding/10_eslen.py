def filtra_parole(lista_parole, n):
    return [parola for parola in lista_parole if len(parola) <= n]

risultato = filtra_parole(["ciao", "a", "eh", "python", "esercizio"], 3)
print("Parole con lunghezza ≤ 3:", risultato)
