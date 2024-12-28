import torch
import torch.nn.functional as F

logits = torch.tensor([[-3.3285, 3.5351]])

# Apply softmax
probabilities = F.softmax(logits, dim=1)

print(probabilities)