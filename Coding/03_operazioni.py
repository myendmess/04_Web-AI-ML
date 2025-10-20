
num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))
operazione = input("Inserisci l'operazione (+, -, *, /): ")

if operazione == "+":
	print("Risultato:", num1 + num2)
elif operazione == "-":
	print("Risultato:", num1 - num2)
elif operazione == "*":
	print("Risultato:", num1 * num2)
elif operazione == "/":
	if num2 != 0:
		print("Risultato:", num1 / num2)
	else:
		print("Errore: divisione per zero!")
else:
	print("Operazione non valida")