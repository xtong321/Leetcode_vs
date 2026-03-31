"""
pytorch-training
Ref: https://neetcode.io/quiz/pytorch-training
"""

model_prediction = model(images)
optimizer.zero_grad()
loss = loss_function(model_prediction, labels)
loss.backward()
optimizer.step()

import torch
import torch.nn as nn
from torchtyping import TensorType

class DigitalRecognition(nn.Module):
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


model = DigitalRecognition()

loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters())

epochs = 5
for epoch in range(epochs):
    for images, lables in train_dataloader:
        images = images.view(images.shape[0], 784)

        # training body

        model_predictiion = model(images)
        optimizer.zero_grad()
        loss = loss_function(model_predictiion, lables)
        loss.backward()
        optimizer.step()


model.eval()
for images, lables in test_dataloader:
    images = images.view(images.shape[0], 784)

    model_prediction = model(images)
    max, idx = torch.max(model_prediction, dim=1)
    for i in range(len(images)):
        plt.imshow(images[i].view(28,28))
        plt.show()
        print(idx[i].item())
        break