n = int(input("Inserisci il numero di righe della piramide: "))

for i in range(1, n + 1):
	spazi = " " * (n - i)
	asterischi = "*" * (2 * i - 1)
	print(spazi + asterischi)