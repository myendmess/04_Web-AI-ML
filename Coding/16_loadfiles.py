import os

# Percorso del file
percorso_file = "text/file.txt"

# Assicurati che la cartella esista
os.makedirs(os.path.dirname(percorso_file), exist_ok=True)

# Scrivi "LOREM IPSUM" nel file
with open(percorso_file, "w", encoding="utf-8") as f:
    f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus convallis sit amet ligula a varius. Phasellus magna nulla, pellentesque non felis nec, porta ultricies purus. Sed ornare mi vitae molestie sollicitudin. Proin nec elit quis ante condimentum ullamcorper vel sit amet felis. Etiam id erat non lorem pretium efficitur a eget lacus. Quisque tellus eros, facilisis nec enim ullamcorper, finibus ornare velit. Nam dapibus ipsum mattis, tincidunt quam sed, egestas turpis. Nullam sed feugiat justo. Morbi bibendum nibh ac velit commodo accumsan. Nulla consectetur, turpis a convallis facilisis, enim elit rutrum sapien, id finibus velit augue ac libero. Fusce venenatis placerat nulla at tempus. Aliquam in magna aliquet, dignissim lorem id, luctus mi.\n")  # una riga

# Classe per leggere e contare le righe
class FileRighe:
    def __init__(self, nome_file):
        self.nome_file = nome_file

    def __str__(self):
        return f"{self.nome_file}"

    @staticmethod
    def conta_righe(nome_file):
        """Legge un file e restituisce il numero di righe"""
        with open(nome_file, "r", encoding="utf-8") as f:
            righe = f.readlines()
        return len(righe)


# Uso della classe
file_obj = FileRighe(percorso_file)
numero_righe = FileRighe.conta_righe(percorso_file)
print(f"Il file '{file_obj}' contiene {numero_righe} righe.")
