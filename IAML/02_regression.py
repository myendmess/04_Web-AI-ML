import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, log_loss

# ==============================
# 2 - REGRESSIONE
# ==============================

# ---- Caso 1: Prezzo case ----
y_true_case = np.array([240000, 330000, 300000, 450000, 230000, 
                        600000, 630000, 370000, 220000, 420000])
y_pred_case = np.array([250000, 310000, 270000, 460000, 220000, 
                        550000, 610000, 380000, 190000, 400000])

mae_case = mean_absolute_error(y_true_case, y_pred_case)
mse_case = mean_squared_error(y_true_case, y_pred_case)
rmse_case = np.sqrt(mse_case)
r2_case = r2_score(y_true_case, y_pred_case)

print("=== Case 1 - Prezzo Case ===")
print(f"MAE  = {mae_case:.2f}")
print(f"MSE  = {mse_case:.2f}")
print(f"RMSE = {rmse_case:.2f}")
print(f"R²   = {r2_case:.3f}")

# ---- Caso 2: Inflazione ----
y_true_infl = np.array([2.5, 3.4, 2.7, 3.0, 2.5])
y_pred_infl = np.array([2.3, 3.1, 3.1, 2.9, 3.2])

mae_infl = mean_absolute_error(y_true_infl, y_pred_infl)
mse_infl = mean_squared_error(y_true_infl, y_pred_infl)
rmse_infl = np.sqrt(mse_infl)
r2_infl = r2_score(y_true_infl, y_pred_infl)

print("\n=== Case 2 - Inflazione ===")
print(f"MAE  = {mae_infl:.2f}")
print(f"MSE  = {mse_infl:.3f}")
print(f"RMSE = {rmse_infl:.3f}")
print(f"R²   = {r2_infl:.3f}")


