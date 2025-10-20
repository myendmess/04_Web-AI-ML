# Simulatore di biglietteria automatica

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QComboBox, QLineEdit, QMessageBox
)

# Lista dei biglietti e prezzi
tipi_biglietto = ["Corsa singola", "Giornaliero", "Settimanale"]
prezzi_biglietto = [1.5, 4.0, 12.0]

class Biglietteria(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Biglietteria Automatica")
        self.setGeometry(200, 200, 350, 200)

        layout = QVBoxLayout()

        # Titolo
        self.label = QLabel("Seleziona il tipo di biglietto:")
        layout.addWidget(self.label)

        # Menu a tendina con i biglietti
        self.combo = QComboBox()
        for i in range(len(tipi_biglietto)):
            self.combo.addItem(f"{tipi_biglietto[i]} -> {prezzi_biglietto[i]} €")
        layout.addWidget(self.combo)

        # Etichetta prezzo
        self.prezzo_label = QLabel("Prezzo: 0 €")
        layout.addWidget(self.prezzo_label)

        # Aggiorna il prezzo quando cambio selezione
        self.combo.currentIndexChanged.connect(self.aggiorna_prezzo)

        # Input per l'importo
        self.input_importo = QLineEdit()
        self.input_importo.setPlaceholderText("Inserisci importo in €")
        layout.addWidget(self.input_importo)

        # Bottone acquisto
        self.btn_acquista = QPushButton("Acquista")
        self.btn_acquista.clicked.connect(self.acquista)
        layout.addWidget(self.btn_acquista)

        self.setLayout(layout)
        self.aggiorna_prezzo()

    def aggiorna_prezzo(self):
        idx = self.combo.currentIndex()
        prezzo = prezzi_biglietto[idx]
        self.prezzo_label.setText(f"Prezzo: {prezzo} €")

    def acquista(self):
        idx = self.combo.currentIndex()
        prezzo = prezzi_biglietto[idx]
        try:
            importo = float(self.input_importo.text())
        except ValueError:
            QMessageBox.warning(self, "Errore", "Inserisci un importo valido.")
            return
        if importo >= prezzo:
            resto = round(importo - prezzo, 2)
            QMessageBox.information(
                self, "Biglietto emesso",
                f"Hai scelto: {tipi_biglietto[idx]} - {prezzo} €\n"
                f"Ecco a te il tuo biglietto!\nResto: {resto} €"
            )
        else:
            QMessageBox.warning(self, "Credito insufficiente", "Credito insufficiente.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    finestra = Biglietteria()
    finestra.show()
    sys.exit(app.exec())
