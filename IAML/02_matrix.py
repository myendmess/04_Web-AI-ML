import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score, classification_report

# -------------------------
# Parte 1 - Matrice binaria
# -------------------------
conf_matrix_1 = np.array([[345, 55],
                          [63, 337]])

# Dati reali e predetti
y_true_1 = (["Cane"]*345 + ["Gatto"]*63 + ["Cane"]*55 + ["Gatto"]*337)
y_pred_1 = (["Cane"]*345 + ["Cane"]*63 + ["Gatto"]*55 + ["Gatto"]*337)

print("=== Parte 1 ===")
print(classification_report(y_true_1, y_pred_1, target_names=["Cane", "Gatto"]))
print("Accuracy:", accuracy_score(y_true_1, y_pred_1))

# -------------------------
# Parte 2 - Matrice multiclasse
# -------------------------
conf_matrix_2 = np.array([[295, 55, 50],
                          [63, 300, 37],
                          [60, 66, 274]])

# Costruzione y_true e y_pred dai conteggi
labels = ["Cane", "Gatto", "Uccello"]

y_true_2, y_pred_2 = [], []
for i, true_label in enumerate(labels):
    for j, pred_label in enumerate(labels):
        count = conf_matrix_2[i, j]
        y_true_2 += [true_label] * count
        y_pred_2 += [pred_label] * count

print("\n=== Parte 2 ===")
print(classification_report(y_true_2, y_pred_2, target_names=labels))
print("Accuracy:", accuracy_score(y_true_2, y_pred_2))