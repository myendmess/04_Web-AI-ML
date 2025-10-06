
class Veicolo:
    def __init__(self, marca, modello, anno, colore):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.colore = colore

    def descrizione(self):
        return f"{self.colore} {self.marca} {self.modello} del {self.anno}"

# Creazione di oggetti della classe Veicolo
auto1 = Veicolo("Toyota", "Corolla", 2020, "Blu")
auto2 = Veicolo("Ford", "Fiesta", 2018, "Rosso")
auto3 = Veicolo("Honda", "Civic", 2021, "Nero")
auto4 = Veicolo("Fiat", "Panda", 2015, "Bianco")
auto5 = Veicolo("Lamborghini Veneno", "Supercar", 2024, "Silver")

# Lista di oggetti Veicolo
lista_auto = [auto1, auto2, auto3, auto4, auto5]

# Stampa delle descrizioni degli oggetti
print("\n".join(auto.descrizione() for auto in lista_auto))