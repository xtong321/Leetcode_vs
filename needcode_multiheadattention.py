"""
multi-head attention implementation with python or pytroch

Key Considerations:
- Scalability: Ensure the embedding dimension is divisible by the number of heads.
- Efficiency: Use PyTorch's optimized matrix operations for better performance.
- Masking: Add support for padding or look-ahead masks if needed for specific tasks 
like sequence generation.

This implementation captures the essence of multi-head attention
 as described in the "Attention Is All You Need" paper.

ref:
https://www.geeksforgeeks.org/deep-learning/how-to-use-pytorchs-nnmultiheadattention/
"""

import torch
import torch.nn as nn

class MultiHeadSelfAttention(nn.Module):
    def __init__(self, embed_dim, num_heads):
        super(MultiHeadSelfAttention, self).__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads

        assert self.head_dim * num_heads == embed_dim, "Embedding dimension must be divisible by number of heads."

        # Linear layers for Query, Key, and Value
        self.q_linear = nn.Linear(embed_dim, embed_dim)
        self.k_linear = nn.Linear(embed_dim, embed_dim)
        self.v_linear = nn.Linear(embed_dim, embed_dim)

        # Output projection
        self.out_proj = nn.Linear(embed_dim, embed_dim)

    def forward(self, x):
        batch_size, seq_length, embed_dim = x.size()

        # Linear projections for Q, K, V
        Q = self.q_linear(x).view(batch_size, seq_length, self.num_heads, self.head_dim).transpose(1, 2)
        K = self.k_linear(x).view(batch_size, seq_length, self.num_heads, self.head_dim).transpose(1, 2)
        V = self.v_linear(x).view(batch_size, seq_length, self.num_heads, self.head_dim).transpose(1, 2)

        # Scaled dot-product attention
        scores = torch.matmul(Q, K.transpose(-2, -1)) / (self.head_dim ** 0.5)
        attention_weights = torch.nn.functional.softmax(scores, dim=-1)
        attention_output = torch.matmul(attention_weights, V)

        # Concatenate heads and project output
        attention_output = attention_output.transpose(1, 2).contiguous().view(batch_size, seq_length, embed_dim)
        return self.out_proj(attention_output)


# Example usage
embed_dim = 64
num_heads = 8
seq_length = 10
batch_size = 2

x = torch.rand(batch_size, seq_length, embed_dim) # Input tensor
multi_head_attention = MultiHeadSelfAttention(embed_dim=embed_dim, num_heads=num_heads)
output = multi_head_attention(x)

print("Output shape:", output.shape) # Expected: [batch_size, seq_length, embed_dim]


## another example
"""
https://www.geeksforgeeks.org/deep-learning/how-to-use-pytorchs-nnmultiheadattention/
Example: Transformer Encoder Layer
To illustrate the usage of nn.MultiheadAttention in a practical scenario, let's 
implement a simple transformer encoder layer. In this example, the TransformerEncoderLayer 
class implements a single layer of a transformer encoder. It uses nn.MultiheadAttention 
for self-attention and includes feedforward neural networks, layer normalization, 
and dropout for regularization.

For below code:
We define the TransformerEncoderLayer class.
We instantiate an object of this class with specific parameters.
We create some dummy input data with a shape of (sequence length, batch size, embedding dimension).
We pass the dummy input through the encoder layer.
We print the shape of the output to ensure it matches the expected shape.

"""
import torch
import torch.nn as nn
import torch.nn.functional as F

class TransformerEncoderLayer(nn.Module):
    def __init__(self, embed_dim, num_heads, dim_feedforward=2048, dropout=0.1):
        super(TransformerEncoderLayer, self).__init__()
        self.self_attn = nn.MultiheadAttention(embed_dim, num_heads, dropout=dropout)
        self.linear1 = nn.Linear(embed_dim, dim_feedforward)
        self.dropout = nn.Dropout(dropout)
        self.linear2 = nn.Linear(dim_feedforward, embed_dim)

        self.norm1 = nn.LayerNorm(embed_dim)
        self.norm2 = nn.LayerNorm(embed_dim)
        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)

    def forward(self, src, src_mask=None, src_key_padding_mask=None):
        src2, _ = self.self_attn(src, src, src, attn_mask=src_mask, key_padding_mask=src_key_padding_mask)
        src = src + self.dropout1(src2)
        src = self.norm1(src)
        src2 = self.linear2(self.dropout(F.relu(self.linear1(src))))
        src = src + self.dropout2(src2)
        src = self.norm2(src)
        return src

# Instantiate the layer
embed_dim = 512
num_heads = 8
layer = TransformerEncoderLayer(embed_dim, num_heads)
dummy_input = torch.rand(10, 32, embed_dim)

# Forward pass through the layer
output = layer(dummy_input)
print(output.shape)

# output: torch.Size([10, 32, 512])