lista_nomi = ["Alice, Bob", "Charlie", "David", "Eve"]
nome_da_uccidere = "  David  ".strip()  # Rimuove gli spazi bianchi

def escludi_nome(lista_nomi, nome_da_uccidere):
    """
    Restituisce una nuova lista con tutti i nomi tranne quello da escludere.
    Gestisce anche eventuali nomi multipli separati da virgola.

    :param lista_nomi: lista di stringhe (nomi)
    :param nome_da_uccidere: stringa, nome da escludere
    :return: lista di stringhe
    """
    # Espande eventuali nomi multipli separati da virgola e rimuove spazi
    nomi_puliti = []
    for item in lista_nomi:
        nomi_puliti.extend([nome.strip() for nome in item.split(',')])
    
    # Filtra il nome da uccidere
    return [nome for nome in nomi_puliti if nome != nome_da_uccidere]

# Otteniamo la lista filtrata
lista_filtrata = escludi_nome(lista_nomi, nome_da_uccidere)

# Stampa senza parentesi e virgolette
print("Lista finale:", ", ".join(lista_filtrata))
print("Nome ucciso:", nome_da_uccidere)
