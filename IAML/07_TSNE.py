# Import librerie
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

# 1️ Caricamento dataset
data = load_wine()
X = data.data       # feature (13)
y = data.target     # etichette (3 classi)

print(f"Numero di feature originali: {X.shape[1]}")

# 2️ Standardizzazione
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3️ PCA - 2 componenti
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 4️ Varianza spiegata
print("Varianza spiegata da ciascuna componente:")
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f"  PC{i+1}: {var:.2%}")
print(f"Varianza totale spiegata: {sum(pca.explained_variance_ratio_):.2%}")

# 7️ t-SNE 2D
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, random_state=42)
X_tsne = tsne.fit_transform(X_scaled)

# 8️ Visualizzazione t-SNE 2D
plt.figure(figsize=(8,6))
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='coolwarm', s=50)
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")
plt.title("t-SNE - Dataset Wine (2 componenti)")
plt.colorbar(label="Classe")
plt.show()

# 9️ t-SNE 3D (opzionale, ma più pesante)
tsne3 = TSNE(n_components=3, perplexity=30, learning_rate=200, random_state=42)
X_tsne3 = tsne3.fit_transform(X_scaled)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_tsne3[:,0], X_tsne3[:,1], X_tsne3[:,2], c=y, cmap='coolwarm', s=50)
ax.set_xlabel("t-SNE 1")
ax.set_ylabel("t-SNE 2")
ax.set_zlabel("t-SNE 3")
plt.title("t-SNE 3D - Dataset Wine")
plt.show()
