import torch
import torch.nn as nn
import torch.nn.functional as F

class SelfAttention(nn.Module):
    def __init__(self, d_in, d_out):
        super().__init__()

        self.q = nn.Linear(d_in, d_out, bias = False)
        self.k = nn.Linear(d_in, d_out, bias = False)
        self.v = nn.Linear(d_in, d_out, bias = False)

    def forward(self, x):
        query = self.q(x)
        key = self.k(x)
        val = self.v(x)

        attn_scores = query @ key.T
        key_dim = key.shape[-1]
        attn = F.softmax(attn_scores / (key_dim ** 0.5), dim=-1)
        return attn @ val


if __name__ == '__main__':
    d_in, d_out = 5, 10
    attn = SelfAttention(d_in, d_out)
    x = torch.rand(2, 5)
    print(attn(x))
    print(attn(x).shape)