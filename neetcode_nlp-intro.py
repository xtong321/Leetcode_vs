"""
https://neetcode.io/problems/nlp-intro/question
Intro to Natural Language Processing

In this problem, you will load in a raw body of text and 
set it up for training. ChatGPT uses the entire text of 
the internet for training, but in this problem we will 
use Amazon product reviews and Tweets from X.

Your task is to encode the input dataset of strings as 
an integer tensor of size 2⋅N×T, where T is the length of 
the longest string. The lexicographically first word 
should be represented as 1, the second should be 2, 
and so on. In the final tensor, list the positive 
encodings, in order, before the negative encodings.

Inputs:
positive - a list of strings, each with positive emotion
negative - a list of strings, each with negative emotion

Example 1:
Input:
positive = ["Dogecoin to the moon"]
negative = ["I will short Tesla today"]

Output: [
  [1.0, 7.0, 6.0, 4.0, 0.0],
  [2.0, 9.0, 5.0, 3.0, 8.0]
]
"""

import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        # First let's get the total set of words
        words = set()
        combined = positive + negative
        for sentence in combined:
            for word in sentence.split():
                words.add(word)

        # Now let's build a mapping
        sorted_list = sorted(list(words))
        word_to_int = {}
        for i, c in enumerate(sorted_list):
            word_to_int[c] = i + 1

        # Write encode() which is used to build the dataset
        def encode(sentence):
            integers = []
            for word in sentence.split():
                integers.append(word_to_int[word])
            return integers
        
        var_len_tensors = []
        for sentence in combined:
            var_len_tensors.append(torch.tensor(encode(sentence)))
        
        return nn.utils.rnn.pad_sequence(var_len_tensors, batch_first = True)
