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


# Step 3: Enable input Tensor


# Step 4: Forward pass through network


# Step 5: Apply Softmax to Convert Logits to probabilities


# Step 6: Predicted Class