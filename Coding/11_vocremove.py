def rimuovi_vocali(s):
    vocali = "aeiouyAEIOUY"
    return ''.join([c for c in s if c not in vocali])

# Esempio d'uso
testo = "i'm not afraid to take a stand, everybody come take my hand, we'll walk this road together, through the storm, whatever " \
"weather, cold or warm, just let you know that you're not alone, holla if you feel like you've been down the same road"
print(rimuovi_vocali(testo))  # Output: testo senza vocali