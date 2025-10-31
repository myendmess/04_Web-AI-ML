# Import librerie
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

# 1️ Caricamento dataset
data = load_wine()
X = data.data       # feature (13)
y = data.target     # etichette (3 classi)

print(f"Numero di feature originali: {X.shape[1]}")

# 2️ Standardizzazione (PCA richiede dati scalati)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3️ PCA - scegli numero componenti (es. 2)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 4️ Varianza spiegata
print("Varianza spiegata da ciascuna componente:")
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f"  PC{i+1}: {var:.2%}")
print(f"Varianza totale spiegata: {sum(pca.explained_variance_ratio_):.2%}")

'''# 5️ Visualizzazione 2D
plt.figure(figsize=(8,6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', s=50)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA - Dataset Wine (2 componenti)")
plt.colorbar(label="Classe")
plt.show()'''

# 6️ Visualizzazione 3D
pca3 = PCA(n_components=3)
X_pca3 = pca3.fit_transform(X_scaled)

print("\nVarianza spiegata (3 componenti):", pca3.explained_variance_ratio_)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_pca3[:,0], X_pca3[:,1], X_pca3[:,2], c=y, cmap='plasma', s=50)
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")
plt.title("PCA 3D - Dataset Wine")
plt.show()
