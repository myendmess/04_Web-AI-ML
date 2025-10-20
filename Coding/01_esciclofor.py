#Chiedi all'utente numeri fino a quando non inserisce 0.

#Utilizza il ciclo while e la keyword break per uscire





def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        numero = int(input("Inserisci un numero (0 per uscire): "))
    except ValueError:
        print("⚠️ Per favore inserisci solo numeri interi.")
        continue

    if numero == 0:
        print("Uscita dal programma.")
        break

    if is_prime(numero):
        print(f"{numero} è un numero primo.")
    else:
        print(f"{numero} non è un numero primo.")
