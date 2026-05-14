"""
implement softmax function with pytorch
"""

import numpy as np
import torch

def manual_softmax(batch_size, num_channels):
    """
    手动实现 Softmax 逻辑
    输入: batch_size (行数), num_channels (列数)
    """
    # 1. 模拟输入数据 (通常是神经网络最后一层的 logits)
    # 形状为 (batch_size, num_channels)
    x = np.random.randn(batch_size, num_channels)
    print("--- 原始输入 (Logits) ---")
    print(x)

    # 2. 数值稳定性处理 (Numerical Stability)
    # 减去每一行的最大值，防止 exp(x) 结果过大导致溢出 (Overflow)
    # keepdims=True 保证减法操作能正确广播 (Broadcast)
    row_max = np.max(x, axis=1, keepdims=True)
    x_stable = x - row_max

    # 3. 计算指数
    exp_x = np.exp(x_stable)

    # 4. 计算每一行的和 (归一化因子)
    row_sum = np.sum(exp_x, axis=1, keepdims=True)

    # 5. 计算最终概率
    softmax_output = exp_x / row_sum
    
    return softmax_output

def softmax(x):
    x_exp = torch.exp(x)
    partition = x_exp.sum(dim=1, keepdim=True)
    return x_exp / partition


x = torch.randn(2, 5)
print(softmax(x))

# 执行示例
batch, channels = 2, 3
result = manual_softmax(batch, channels)

print("\n--- Softmax 输出 (概率分布) ---")
print(result)
print("\n每行之和 (验证是否为 1):", np.sum(result, axis=1))