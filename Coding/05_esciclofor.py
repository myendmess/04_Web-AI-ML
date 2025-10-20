'''Chiedi all’utente 5 numeri e stampali solo se dispari. Qui puoi usare un for su range(5) e dentro un continue se il numero è pari.'''

numeri_dispari = []
for i in range(5):
    numero = int(input("Inserisci un numero: "))
    if numero % 2 == 0:
        continue
    numeri_dispari.append(numero)
print("Numeri dispari inseriti:", numeri_dispari)