# Simulatore di distributore di merendine con PyQt6

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QMessageBox
)

# Liste dei prodotti e prezzi
prodotti = ["Patatine", "Cioccolato", "Biscotti", "Succo"]
prezzi = [1.5, 2.0, 1.2, 1.8]

# Valori validi di monete e banconote
valori_validi = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20]


class Distributore(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Distributore di Merendine")
        self.setGeometry(200, 200, 400, 300)

        self.credito = 0.0

        layout = QVBoxLayout()

        # Titolo
        self.label = QLabel("=== Distributore di Merendine ===")
        layout.addWidget(self.label)

        # Menu prodotti
        self.combo = QComboBox()
        for i in range(len(prodotti)):
            self.combo.addItem(f"{prodotti[i]} -> {prezzi[i]} €")
        layout.addWidget(self.combo)

        # Etichetta credito
        self.credito_label = QLabel(f"Credito attuale: {self.credito} €")
        layout.addWidget(self.credito_label)

        # Sezione monete/banconote
        layout.addWidget(QLabel("Inserisci moneta/banconota:"))
        monete_layout = QHBoxLayout()

        for val in valori_validi:
            btn = QPushButton(str(val))
            btn.clicked.connect(lambda _, v=val: self.aggiungi_credito(v))
            monete_layout.addWidget(btn)

        layout.addLayout(monete_layout)

        # Bottone acquista
        self.btn_acquista = QPushButton("Acquista")
        self.btn_acquista.clicked.connect(self.acquista)
        layout.addWidget(self.btn_acquista)

        # Bottone esci
        self.btn_exit = QPushButton("Esci")
        self.btn_exit.clicked.connect(self.esci)
        layout.addWidget(self.btn_exit)

        self.setLayout(layout)

    def aggiorna_credito(self):
        self.credito_label.setText(f"Credito attuale: {round(self.credito, 2)} €")

    def aggiungi_credito(self, valore):
        self.credito += valore
        self.aggiorna_credito()

    def acquista(self):
        idx = self.combo.currentIndex()
        prodotto = prodotti[idx]
        prezzo = prezzi[idx]

        if self.credito >= prezzo:
            self.credito -= prezzo
            self.aggiorna_credito()
            QMessageBox.information(
                self, "Acquisto riuscito",
                f"Hai comprato: {prodotto}\nResto attuale: {round(self.credito, 2)} €"
            )
        else:
            QMessageBox.warning(
                self, "Credito insufficiente",
                f"Credito disponibile: {round(self.credito, 2)} €\nPrezzo {prodotto}: {prezzo} €"
            )

    def esci(self):
        if self.credito > 0:
            QMessageBox.information(
                self, "Uscita",
                f"Grazie per aver usato il distributore!\nResto restituito: {round(self.credito, 2)} €"
            )
        else:
            QMessageBox.information(
                self, "Uscita",
                "Grazie per aver usato il distributore!"
            )
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    finestra = Distributore()
    finestra.show()
    sys.exit(app.exec())

''' --------ignore--------

Distributore di merendine con PyQt6

Ogni pulsante delle monete è collegato alla funzione aggiungi_credito creato con lambda per non dichiararlo più volte.

--Metodi principali--

aggiorna_credito(line78): aggiorna a schermo il credito attuale.

aggiungi_credito(valore)(line69): aggiunge il valore al credito e aggiorna la label.

--acquista():--

controlla se il credito è sufficiente per comprare il prodotto selezionato

se sì → scala il prezzo, aggiorna e mostra un messaggio di successo

se no → mostra un avviso di credito insufficiente 

utilizza QMessageBox per i messaggi pop up
'''