


voto=int(input("Inserisci il numero da 0 a 10: "))
if 0 < voto < 6:
    print("Insufficiente")
elif 6 <= voto < 8:
    print("Sufficiente")
elif 8 <= voto < 10:
    print("Buono")
elif voto == 10:
    print("Ottimo")
else:
    print("Valore non valido")