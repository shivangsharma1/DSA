import torch
import torch.nn as nn
import torch.nn.functional as F


class CausalAttention(nn.Module):
    def __init__(self, d_in, d_out, context_len, bias=False, drop = 0.1):
        super().__init__()
        self.q = nn.Linear(d_in, d_out, bias=False)
        self.k = nn.Linear(d_in, d_out, bias=False)
        self.v = nn.Linear(d_in, d_out, bias=False)
        self.drop = nn.Dropout(drop)
        self.context_len = context_len
        self.register_buffer(
            "mask",
            torch.triu(torch.ones(self.context_len, self.context_len), diagonal=1),
        )

    def forward(self, x):
        batch, context_len, d_in = x.shape
        query = self.q(x)
        key = self.k(x)
        val = self.v(x)

        attn_score = query @ key.transpose(1, 2)
        attn_score.masked_fill_(self.mask.bool()[:context_len, :context_len], -torch.inf)
        attn = F.softmax(attn_score / (key.shape[-1] ** 0.5), dim = -1)    
        attn = self.drop(attn)

        return attn @ val



if __name__ == "__main__":
    d_in, d_out = 5, 5
    x = torch.rand(d_in, d_out)
    x_in = torch.stack((x, x), dim=0)
    print(x_in.shape)

    causal = CausalAttention(d_in, d_out, x_in.shape[1])
    print(causal(x_in))

