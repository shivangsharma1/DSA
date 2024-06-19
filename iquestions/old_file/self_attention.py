import numpy as np

def self_attention(query, key, value):
    # Calculate the attention scores
    scores = np.matmul(query, key.T)
    
    # Apply softmax to normalize the scores
    attention_weights = np.exp(scores) / np.sum(np.exp(scores), axis=-1, keepdims=True)
    print("num " ,np.exp(scores))
    print("Denom " ,np.sum(np.exp(scores), axis=-1))
    # Calculate the weighted sum of values
    weighted_sum = np.matmul(attention_weights, value)
    
    return weighted_sum, attention_weights

# Sample input values
query = np.array([[1, 2, 3], [4, 5, 6]])  # shape: (batch_size, seq_len_q, d_model)
key = np.array([[1, 0, 1], [1, 1, 0]])     # shape: (batch_size, seq_len_k, d_model)
value = np.array([[0, 1, 0], [1, 0, 1]])   # shape: (batch_size, seq_len_v, d_model)

# Perform self-attention
weighted_sum, attention_weights = self_attention(query, key, value)

print("Weighted Sum:")
print(weighted_sum)
print("\nAttention Weights:")
print(attention_weights)
