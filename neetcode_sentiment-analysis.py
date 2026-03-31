"""
https://neetcode.io/problems/sentiment-analysis/question
Sentiment Analysis

Your task is to implement a neural network that can 
recognize positive or negative emotion in an input 
sentence. This application of work embeddings is the 
first step in building ChatGPT. To learn more about 
word embeddings, check out this video.

The background video is critical to completely 
understanding the ML concepts involved in this problem.

For the model architecture, first use an embedding layer 
of size 16. Compute the average of the embeddings to 
remove the time dimension, and end with a single-neuron 
linear layer followed by a sigmoid. The averaging is 
called the "Bag of Words" model in NLP.

Implement the constructor and forward() pass that outputs 
the model's prediction as a number between 0 and 1 
(completely negative vs. completely positive). Do not 
train the model.

Inputs:
- vocabulary_size - the number of different words the model 
should be able to recognize
- x - a list of strings, each with negative emotion

Example:
Input:
vocabulary_size = 170,000
x = [
  [2.0, 7.0, 14.0, 8.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],    // "The movie was okay"
  [1.0, 4.0, 12.0, 3.0, 10.0, 5.0, 15.0, 11.0, 6.0, 9.0, 13.0, 7.0] // "I don't think anyone should ever waste their money on this movie"
]

Output: [
  [0.5], [0.1]
]
Explanation: The output is provided to show the expected shape of the inputs and outputs. Your exact model prediction won't match this since you are not training the model.
"""

import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution(nn.Module):
    def __init__(self, vocabulary_size: int):
        super().__init__()
        torch.manual_seed(0)
        self.embedding_layer = nn.Embedding(vocabulary_size, 16)
        self.linear_layer = nn.Linear(16, 1)
        self.sigmoid_layer = nn.Sigmoid()

    def forward(self, x: TensorType[int]) -> TensorType[float]:
        embeddings = self.embedding_layer(x)
        averaged = torch.mean(embeddings, axis = 1)
        projected = self.linear_layer(averaged)
        return torch.round(self.sigmoid_layer(projected), decimals=4)
