'''Data una lista di numeri [3, 5, 7, -2, 10, 12], stampali finché non incontri un numero negativo. Usa break.'''



numeri = [3, 5, 7, -2, 10, 12]
for numero in numeri:
    if numero < 0:
        break
    print(numero)