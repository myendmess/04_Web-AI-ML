import tensorflow as tf
from tensorflow.keras.utils import plot_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist

# Carica dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalizza
X_train, X_test = X_train / 255.0, X_test / 255.0

# Crea il modello
model = Sequential([
    Flatten(input_shape=(28, 28)),  # converte immagine 28x28 in vettore 784
    Dense(64, activation='relu'),   # hidden layer
    Dense(10, activation='softmax') # output layer
])

# Compila e addestra
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))

# Valuta il modello
loss, acc = model.evaluate(X_test, y_test)
print(f"Accuratezza: {acc:.2f}")
plot_model(model, show_shapes=True, show_layer_names=True, to_file="05_imgmodel.png")