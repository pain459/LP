import torch
import torch.nn as nn
import torch.nn.functional as F

# Step 1: Define the neural network
class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(SimpleNN, self).__init__()
        # Define layers
        self.hidden_layer = nn.Linear(input_size, hidden_size)
        self.output_layer = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        # Hidden layer with ReLU activation
        hidden_out = F.relu(self.hidden_layer(x))
        # Output layer (logits)
        logits = self.output_layer(hidden_out)
        return logits


# Step 2: Instantiate the network
input_size = 5  # Example input size (5 tokens represented as numbers)
hidden_size = 3  # Hidden layer has 3 neurons
num_classes = 3  # Output layer for 3 classes (postive, neutral, negative)
model = SimpleNN(input_size, hidden_size, num_classes)

# Step 3: Enable input Tensor
# Simulate input data (embeddings for 5 tokens)
example_input = torch.tensor([[0.5, 1.0, -0.5, 2.0, -1.0]])  # shape: (1, 5)

# Step 4: Forward pass through network
logits = model(example_input)  # raw logits
print("Logits (Raw Outputs):")
print(logits)

# Step 5: Apply Softmax to Convert Logits to probabilities
probabilities = F.softmax(logits, dim=1)
print("\nProbabilities (After Softmax):")
print(probabilities)

# Step 6: Predicted Class
predicted_class = torch.argmax(probabilities, dim=1)
print("\nPredicted Class:", predicted_class.item())