import numpy as np

# === Dati ===
infl_reale = np.array([2.5, 3.4, 2.7, 3.0, 2.5])
infl_pred  = np.array([2.3, 3.1, 3.1, 2.9, 3.2])

# Differenza a = y - y^
a = infl_reale - infl_pred

# === Huber Loss ===
delta = 0.3

def huber_loss(a, delta):
    abs_a = np.abs(a)
    return np.where(abs_a <= delta, 0.5 * a**2, delta * (abs_a - 0.5 * delta))

HL = huber_loss(a, delta)
HL_totale = np.sum(HL)
HL_media = np.mean(HL)

# === Log-Cosh Loss ===
def log_cosh_loss(a):
    return np.log(np.cosh(a))

LCL = log_cosh_loss(a)
LCL_totale = np.sum(LCL)
LCL_media = np.mean(LCL)

# === Output ===
print("=== Huber Loss ===")
for i, val in enumerate(HL):
    print(f"Anno {2026+i}: a={a[i]:>5.2f}  HL={val:.6f}")
print(f"HL Totale = {HL_totale:.6f}")
print(f"HL Media  = {HL_media:.6f}\n")

print("=== Log-Cosh Loss ===")
for i, val in enumerate(LCL):
    print(f"Anno {2026+i}: a={a[i]:>5.2f}  LCL={val:.6f}")
print(f"LCL Totale = {LCL_totale:.6f}")
print(f"LCL Media  = {LCL_media:.6f}")
