import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import plot_model
import matplotlib.pyplot as plt

# 1. Load dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 2. Normalize pixels (0–1)
X_train, X_test = X_train / 255.0, X_test / 255.0

# 3. Build improved model
model = Sequential([
    Flatten(input_shape=(28, 28)),               # Input: 28x28 -> 784
    Dense(256, activation='relu', kernel_initializer='he_normal'),
    Dropout(0.3),
    Dense(128, activation='relu', kernel_initializer='he_normal'),
    Dropout(0.3),
    Dense(64, activation='relu', kernel_initializer='he_normal'),
    Dense(10, activation='softmax')              # Output layer (10 classes)
])

# 4. Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 5. Train
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=128,
    validation_data=(X_test, y_test),
    verbose=1
)

# 6. Evaluate
loss, acc = model.evaluate(X_test, y_test)
print(f"\nFinal test accuracy: {acc:.4f}")

# 7. Save model architecture image
plot_model(model, show_shapes=True, show_layer_names=True, to_file="mnist_model_improved.png")

# 8. Plot training history
plt.figure(figsize=(12, 5))

# Accuracy
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Accuracy Over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)

# Loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss Over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("mnist_training_graph.png", dpi=150)
plt.show()
