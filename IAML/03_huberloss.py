import numpy as np

# Dati
y_true = np.array([240, 330, 300, 450, 230, 600, 630, 370, 220, 420])
y_pred = np.array([250, 310, 270, 460, 220, 550, 610, 380, 190, 400])

# Differenza (a = y - y^)
a = y_true - y_pred

# ----- Huber Loss -----
delta = 50000

def huber_loss(a, delta):
    abs_a = np.abs(a)
    return np.where(abs_a <= delta, 0.5 * a**2, delta * (abs_a - 0.5 * delta))

HL = huber_loss(a, delta)
HL_totale = np.sum(HL)
HL_media = np.mean(HL)

# ----- Log-Cosh Loss -----
# Formula: L(a) = log(cosh(a))
# Più stabile numericamente
def log_cosh_loss(a):
    return np.log(np.cosh(a))

LCL = log_cosh_loss(a)
LCL_totale = np.sum(LCL)
LCL_media = np.mean(LCL)

# ----- Output -----
print("=== Huber Loss ===")
for i, val in enumerate(HL):
    print(f"Sample {i+1}: a={a[i]:>6}  HL={val:.4f}")
print(f"HL Totale = {HL_totale:.4f}")
print(f"HL Media  = {HL_media:.4f}\n")

print("=== Log-Cosh Loss ===")
for i, val in enumerate(LCL):
    print(f"Sample {i+1}: a={a[i]:>6}  LCL={val:.4f}")
print(f"LCL Totale = {LCL_totale:.4f}")
print(f"LCL Media  = {LCL_media:.4f}")
