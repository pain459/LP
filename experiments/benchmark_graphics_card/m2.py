# TensorFlow or PyTorch for Deep Learning Benchmarks


import tensorflow as tf
import time

# Create a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1024, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Generate some random data
x_train = tf.random.normal((10000, 784))
y_train = tf.random.uniform((10000,), minval=0, maxval=10, dtype=tf.int64)

# Train the model and measure time
start_time = time.time()
model.fit(x_train, y_train, epochs=10, batch_size=256, verbose=0)
end_time = time.time()

print(f"Time taken for training: {end_time - start_time:.4f} seconds")
