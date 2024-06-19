import torch
import torch.nn as nn
torch.manual_seed(0)

class SelfHeadAttention(nn.Module):
    def __init__(self, embedded_dim, attention_dim):
        super().__init__()
        self.query = nn.Linear(embedded_dim, attention_dim, bias=False)
        self.key = nn.Linear(embedded_dim, attention_dim, bias=False)
        self.value = nn.Linear(embedded_dim, attention_dim, bias=False)

    def forward(self, embeds, mask=False):
        query = self.query(embeds)
        key = self.key(embeds)
        val = self.value(embeds)

        scores = query @ torch.transpose(key, 1, 2)
        _, context_length, attention = key.shape
        scores = scores / (attention ** 0.5)

        premask = torch.tril(torch.ones(context_length, context_length))
        mask = premask == 0
        scores = scores.masked_fill(mask, float('-inf'))
        scores = nn.functional.softmax(scores, dim=2)

        return scores @ val

if __name__ == '__main__':
    embeds = torch.rand(2, 2, 2)
    embedded_dim, attention_dim = 2, 3
    obj = SelfHeadAttention(embedded_dim, attention_dim)
    print(obj.forward(embeds, mask=True))