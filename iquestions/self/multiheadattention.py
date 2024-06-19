from self_attention import SelfHeadAttention
import torch
import torch.nn as nn


class MultiHeadAttention(nn.Module):
    def __init__(self, attention_dim, num_heads=4):
        super().__init__()
        torch.manual_seed(0)

        self.list = nn.ModuleList()
        for _ in range(num_heads):
            self.list.append(SelfHeadAttention(attention_dim, attention_dim//num_heads))

    def forward(self, embedded):
        outputs = []
        for head in self.list:
            outputs.append(head(embedded))

        cat = torch.cat(outputs, dim=-1)
        return torch.round(cat, decimals=4)
    

if __name__ == '__main__':
    embedded = torch.rand(2, 2, 6)
    attention_dim, num_heads = 6, 3

    obj = MultiHeadAttention(attention_dim, num_heads)
    out = obj(embedded)
    print(out)
