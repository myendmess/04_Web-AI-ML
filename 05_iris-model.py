# Import librerie
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# Carica dataset
iris = load_iris()
X, y = iris.data, iris.target

# Normalizzazione
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Suddividi in train e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crea il modello sequenziale
model = Sequential([
    Dense(8, activation='relu', input_shape=(4,)),  # input layer + 1 hidden layer
    Dense(3, activation='softmax')                  # output layer (3 classi)
])

# Compila il modello
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Addestra il modello
history = model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test), verbose=0)

# Valuta il modello
loss, acc = model.evaluate(X_test, y_test)
print(f"Accuratezza: {acc:.2f}")
