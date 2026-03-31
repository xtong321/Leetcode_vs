"""
Pytorch Basics
Ref: https://neetcode.io/problems/basics-of-pytorch
PyTorch is the industry standard library for deep learning and was used to train ChatGPT. Checkout the first 9 minutes of this video for a summary of the basic functions.
You will use built in PyTorch functions to manipulate tensors. These are important to understand before building more interesting & powerful neural networks.

Your tasks:
- Reshape an M×N tensor into a (M⋅N//2)×2 tensor.
- Find the average of every column in a tensor.
- Combine an M×N tensor and a M×M tensor into a M×(M+N) tensor.
- Calculate the mean squared error loss between a prediction and target tensor.

Inputs:
- to_reshape - a tensor to reshape
- to_avg - a tensor to average column wise
- cat_one - the first tensor to concatenate
- cat_two - the second tensor to concatenate
- prediction - the output tensor of a model
- target - the true labels for the model inputs

Example (Reshape):
Input:
to_reshape = [
  [1.0, 1.0, 1.0, 1.0],
  [1.0, 1.0, 1.0, 1.0],
  [1.0, 1.0, 1.0, 1.0]
]
Output:
[
  [1.0, 1.0],
  [1.0, 1.0],
  [1.0, 1.0],
  [1.0, 1.0],
  [1.0, 1.0],
  [1.0, 1.0]
]

Example (Average):
Input: 
to_avg = [
  [0.8088, 1.2614, -1.4371],
  [-0.0056, -0.2050, -0.7201]
]
Output:
[0.4016, 0.5282, -1.0786]

Example (Concatenate):
Input:
cat_one = [
  [1.0, 1.0, 1.0],
  [1.0, 1.0, 1.0]
]
cat_two = [
  [1.0, 1.0],
  [1.0, 1.0]
]
Output:
[
  [1.0, 1.0, 1.0, 1.0, 1.0],
  [1.0, 1.0, 1.0, 1.0, 1.0]
]

Example (Get Loss):
Input:
prediction = [0.0, 1.0, 0.0, 1.0, 1.0]
target = [1.0, 1.0, 0.0, 0.0, 0.0]

Output:
0.6
"""

import torch
import torch.nn
from torchtyping import TensorType
import numpy as np

# Helpful functions:
# https://pytorch.org/docs/stable/generated/torch.reshape.html
# https://pytorch.org/docs/stable/generated/torch.mean.html
# https://pytorch.org/docs/stable/generated/torch.cat.html
# https://pytorch.org/docs/stable/generated/torch.nn.functional.mse_loss.html

# Round your answers to 4 decimal places using torch.round(input_tensor, decimals = 4)
class Solution:
    # Reshape an M×N tensor into a (M⋅N//2)×2 tensor.
    def reshape(self, to_reshape: TensorType[float]) -> TensorType[float]:
        # torch.reshape() will be useful - check out the documentation
        M, N = to_reshape.shape
        reshaped = torch.reshape(to_reshape, (M * N // 2, 2))
        return torch.round(reshaped, decimals=4)
        #pass

    # Find the average of every column in a tensor.
    def average(self, to_avg: TensorType[float]) -> TensorType[float]:
        # torch.mean() will be useful - check out the documentation
        averaged = torch.mean(to_avg, dim = 0)
        return torch.round(averaged, decimals=4)
        #pass
    
    # Combine an M×N tensor and a M×M tensor into a M×(M+N) tensor.
    def concatenate(self, cat_one: TensorType[float], cat_two: TensorType[float]) -> TensorType[float]:
        # torch.cat() will be useful - check out the documentation
        concatenated = torch.cat((cat_one, cat_two), dim = 1)
        return torch.round(concatenated, decimals=4)
        #pass

    # Calculate the mean squared error loss between a prediction and target tensor.
    def get_loss(self, prediction: TensorType[float], target: TensorType[float]) -> TensorType[float]:
        # torch.nn.functional.mse_loss() will be useful - check out the documentation
        loss = torch.nn.functional.mse_loss(prediction, target)
        return torch.round(loss, decimals=4)
        # pass

if __name__ == "__main__":
    # Example (Reshape):
    to_reshape = [
        [1.0, 1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0, 1.0]
    ]    
    '''Output: [
        [1.0, 1.0],
        [1.0, 1.0],
        [1.0, 1.0],
        [1.0, 1.0],
        [1.0, 1.0],
        [1.0, 1.0]
    ]'''
    to_numpy = np.array(to_reshape) # list to numpy
    #to_tensor = torch.from_numpy(to_numpy).float() # numpy to tensor
    to_tensor = torch.Tensor(to_reshape) # list to tensor
    print(Solution().reshape(to_tensor))

    # Example (Average):
    to_avg = [
        [0.8088, 1.2614, -1.4371],
        [-0.0056, -0.2050, -0.7201]
    ]    
    '''Output:    [0.4016, 0.5282, -1.0786]
    '''
    to_avg_tensor = torch.Tensor(to_avg)
    print(Solution().average(to_avg_tensor))

    #Example (Concatenate):
    cat_one = [
        [1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0]
    ]
    cat_two = [
        [1.0, 1.0],
        [1.0, 1.0]
    ]
    '''Output:
    [
        [1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 1.0, 1.0, 1.0, 1.0]
    ]'''
    cat_one = torch.Tensor(cat_one)
    cat_two = torch.Tensor(cat_two)
    print(Solution().concatenate(cat_one, cat_two))

    #Example (Get Loss):
    prediction = [0.0, 1.0, 0.0, 1.0, 1.0]
    target = [1.0, 1.0, 0.0, 0.0, 0.0]
    #Output: 0.6
    prediction = torch.Tensor(prediction)
    target = torch.Tensor(target)
    print(Solution().get_loss(prediction, target))