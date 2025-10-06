#Data una stringa, stampa solo le vocali che contiene.

stringa = input("Inserisci una parola: ")
vocali = "aeiou"
vocali_nella_stringa = [char for char in stringa if char in vocali]
print("Vocali nella parola inserita:", vocali_nella_stringa)
if not vocali_nella_stringa:
    print("Nessuna vocale trovata")
