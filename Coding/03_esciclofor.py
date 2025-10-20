''' Scrivi un algoritmo che data una lista di nomi, quando trovo un nome specifico, stampo quel nome ed esco fuori dal ciclo.'''


def is_heisenberg_prime(walter):
    """
    Controllo se un numero è primo.
    Walter White approverebbe solo se il numero è 'puro'
    """
    if walter <= 1:
        return False
    for jesse in range(2, int(walter**0.5) + 1):
        if walter % jesse == 0:
            return False
    return True

while True:
    try:
        saul = int(input("Yo, inserisci un numero (0 per uscire): "))
    except ValueError:
        print("Saul Goodman dice: inserisci solo numeri interi!")
        continue

    if saul == 0:
        print("Heisenberg ha chiuso il laboratorio.")
        break

    if is_heisenberg_prime(saul):
        print(f"{saul} è puro al 99%. Numero primo approvato da Gus Fring.")
    else:
        print(f"{saul} non è primo. Jesse dice: 'Yeah, science, b***h!'")
