import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Sample dataset
sentences = [
    'I love this movie!',
    'This movie is great.',
    'Such an amazing film.',
    'I hated every moment of it.',
    'Terrible movie, would not recommend.'
]
labels = [1, 1, 1, 0, 0]  # 1 for positive sentiment, 0 for negative sentiment

# Tokenize the sentences
tokenizer = Tokenizer(num_words=100, oov_token='<OOV>')
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

# Convert sentences to sequences
sequences = tokenizer.texts_to_sequences(sentences)
padded_sequences = pad_sequences(sequences, maxlen=10, padding='post')

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(word_index) + 1, output_dim=16, input_length=10),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(6, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

# Convert labels to numpy array
import numpy as np
labels = np.array(labels)

# Train the model
model.fit(padded_sequences, labels, epochs=10, verbose=2)

# Test the model
test_sentences = [
    'I really enjoyed it!',
    'Not a good experience.'
]
test_sequences = tokenizer.texts_to_sequences(test_sentences)
padded_test_sequences = pad_sequences(test_sequences, maxlen=10, padding='post')
predictions = model.predict(padded_test_sequences)
print(predictions)
