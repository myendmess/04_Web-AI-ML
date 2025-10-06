import numpy as np
from sklearn.metrics import log_loss

# ==============================
# 3 - LOSS FUNCTIONS
# ==============================

# ---- Cross Entropy binaria ----
# Caso 1: y=1, p=0.4
y_true_ce1 = np.array([1])
y_pred_ce1 = np.array([[0.6, 0.4]])  # [p0=0.6, p1=0.4]
ce1 = log_loss(y_true_ce1, y_pred_ce1, labels=[0,1])

# Caso 2: y=0, p=0.7
y_true_ce2 = np.array([0])
y_pred_ce2 = np.array([[0.7, 0.3]])  # [p0=0.7, p1=0.3]
ce2 = log_loss(y_true_ce2, y_pred_ce2, labels=[0,1])

print("\n=== Case 1 - Cross Entropy ===")
print(f"CE (y=1, p=0.4) = {ce1:.3f}")
print(f"CE (y=0, p=0.7) = {ce2:.3f}")

# ---- Multiclass Cross Entropy ----
# y = cane (classe 0), predizioni: cane=0.4, gatto=0.2, uccello=0.4
y_true_mce = np.array([0])  # Cane
y_pred_mce = np.array([[0.4, 0.2, 0.4]])
mce = log_loss(y_true_mce, y_pred_mce, labels=[0,1,2])

print("\n=== Case 2 - Multiclass CE ===")
print(f"MCE = {mce:.3f}")

# ---- Hinge Loss ----
# Formula: HL = max(0, 1 - y * y_hat), con y ∈ {-1, +1}
y = 1
y_hat = 0.7
hl = max(0, 1 - y * y_hat)

print("\n=== Case 3 - Hinge Loss ===")
print(f"HL = {hl:.3f}")
