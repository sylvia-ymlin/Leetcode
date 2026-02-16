import torch
import torch.nn as nn

class MHA(nn.Module):
    def __init__(self, dim, head_num):
        super().__init__()
        assert dim % head_num == 0, "dim should be divisible by head_num"
        self.head_num = head_num
        self.head_dim = dim // head_num
        self.qkv = nn.Linear(dim, dim * 3)
        self.o = nn.Linear(dim, dim)

    def forward(self, x, ids=None, causal=False, kv_cache=None):
        bs, seq_len, dim = x.shape
        qkv = self.qkv(x)  # (bs, seq_len, dim * 3)
        q, k, v = torch.chunk(qkv, 3, dim=-1)

        # reshape to multiple heads
        q = q.view(bs, seq_len, self.head_num, self.head_dim).permute(0, 2, 1, 3)
        k = k.view(bs, seq_len, self.head_num, self.head_dim).permute(0, 2, 3, 1)
        v = v.view(bs, seq_len, self.head_num, self.head_dim).permute(0, 2, 1, 3)

        # add kv_cache if provided
        if kv_cache is not None:
            k_cache, v_cache = kv_cache
            k = torch.cat([k_cache, k], dim=-1)
            v = torch.cat([v_cache, v], dim=-2)

        q = q / (self.head_dim ** 0.5)
        score = q @ k  # (bs, head_num, seq_len, seq_len)

        if ids is not None:
            # segment masking
            seg_i = ids.unsqueeze(1).unsqueeze(2)  # (bs, 1, 1, seq_len)
            seg_j = ids.unsqueeze(1).unsqueeze(3)  # (bs, 1, seq_len, 1)
            seg_mask = seg_i != seg_j
            score = score.masked_fill(seg_mask, float('-inf'))

        if causal:
            # causal masking (upper triangular)
            mask = torch.triu(torch.ones((seq_len, seq_len), device=x.device), diagonal=1).bool()
            mask = mask.unsqueeze(0).unsqueeze(0)  # (1, 1, seq_len, seq_len)
            score = score.masked_fill(mask, float('-inf'))

        # stabilize softmax
        score = score - torch.max(score, dim=-1, keepdim=True)[0]
        attn = torch.softmax(score, dim=-1)

        out = attn @ v
        out = out.permute(0, 2, 1, 3).reshape(bs, seq_len, dim)
        out = self.o(out)

        if kv_cache is not None:
            return out, (k, v)
        else:
            return out