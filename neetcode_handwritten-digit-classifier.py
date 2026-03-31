"""
Digit Classifier
Ref: https://neetcode.io/problems/handwritten-digit-classifier
course: https://www.youtube.com/watch?v=SxwtCEDHXe8&t=553s

Your task is to implement a neural network that can recognize black and white 
images of handwritten digits. This is a simple but powerful application 
of neural networks. To learn about coding neural networks in PyTorch, watch this 10 minute clip.
For the model architecture, first use linear layer with 512 neurons 
follwed by a ReLU activation, as well as a dropout layer with probability 
p = 0.2 that precedes a final Linear layer with 10 neurons and a 
sigmoid activation. Each output neuron corresponds to a digit from 0 to 9, 
where each value is the probability that the input image is the corresponding digit.

Input:
images - one or more 28×28 black and white images of handwritten digits. 
len(images) > 0 and len(images[i]) = 28 * 28 for 0 <= i < len(images).
Write the artchitecture / constructor and the forward() pass that returns 
the model's prediction. Do not write the training loop (or gradient descent) 
to minimize the error.

Example 1:
Handwritten Digit Classifier

Input:
images = [[0, 0, 0, ... (many indices omitted), 254, 255, ... 0]]

Output:
[[0, 0, 0.1, 0, 0, 0, 0, 0.9, 0, 0]]
Note: The example is provided to understand the format of the output. Your exact model prediction won't match this since you are not training the model.
"""

import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution(nn.Module):
    def __init__(self):
        super().__init__()
        torch.manual_seed(0)        
        self.first_linear = nn.Linear(784, 512)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.2)
        self.projection = nn.Linear(512, 10)
        self.sigmoid = nn.Sigmoid()
        # Define the architecture here
    
    def forward(self, images: TensorType[float]) -> TensorType[float]:
        torch.manual_seed(0)
        out = self.sigmoid(self.projection(self.dropout(self.relu(self.first_linear(images)))))
        return torch.round(out, decimals=4)
        # Return the model's prediction to 4 decimal places
