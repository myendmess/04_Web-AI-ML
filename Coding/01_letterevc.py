#Esercizio: Dato un carattere singolo, tipo 'a' voglio controllare se sia una vocale; Se è vero stampa "vocale" altrimenti "consonante"


lettera = input("Inserisci un carattere: ")
if lettera in "aeiou":
    print("vocale")
else:
    if lettera.isalpha() and len(lettera) == 1:
        print("consonante")
    else:
        print("carattere non valido")
