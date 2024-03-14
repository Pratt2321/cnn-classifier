import os
os.environ['TBLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
from tensorflow.keras import layers, models

height = 64  # Replace with the actual height of your input data
width = 64   # Replace with the actual width of your input data
channels = 64  # Replace with the actual number of channels in your input data (e.g., 1 for grayscale, 3 for RGB)

# Define your neural network architecture
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(height, width, channels)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='relu')  # 1 output node for binary classification
])

# Compile the model
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

# Train the model with your denoised EEG graphs
model.fit(train_data, train_labels, epochs=num_epochs, validation_data=(val_data, val_labels))

# Evaluate the model
test_loss, test_acc = model.evaluate(test_data, test_labels)
print(f'Test accuracy: {test_acc}')