import torch
import torch.nn as nn
torch.manual_seed(0)

class SelfAttention(nn.Module):
    def __init__(self, embedding_dim, attention_dim):
        super().__init__()
        self.key = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.query = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.value = nn.Linear(embedding_dim, attention_dim, bias=False)

    def forward(self, embeds):
        query = self.query(embeds)
        key = self.key(embeds)
        value = self.value(embeds)

        print("Query: ", query.shape)
        print("key: ", key.shape)
        print("value: ", value.shape)

        scores = query @ torch.transpose(key, 1, 2)
        _, context_len, atten_dim = key.shape
        scores = scores / (atten_dim ** 0.5)

        premask = torch.tril(torch.ones(context_len, context_len))
        mask = premask == 0
        scores = scores.masked_fill(mask, float('-inf'))

        scores = nn.functional.softmax(scores, dim=-1)

        return (scores @ value).shape
    

if __name__ == '__main__':
    embedded_dim, attention_dim = 2, 8
    embeds = torch.rand(2, 2, 2)
    obj = SelfAttention(embedded_dim, attention_dim)
    print(obj.forward(embeds))