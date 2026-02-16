
def sinusoidal_embedding(seq_len, dim):
    assert dim % 2 == 0, "dim must be even"
    half = dim // 2

    freq = torch.pow(10000, -(2 * torch.arange(half) / dim))
    pos = torch.arange(seq_len, dtype=freq.dtype).view(seq_len, 1)

    sin = torch.sin(pos * freq.view(1, half))
    cos = torch.cos(pos * freq.view(1, half))

    return torch.cat([sin, cos], dim=-1)  # concat along last dim, don't need to be interleaved (sin0,cos0,sin1,cos1,... as in paper)

def apply_rope(x, max_seq_len=512):
    # apply before calculate score
    bas, head_num, seq_len, dim = x.shape
    assert dim % 2 == 0, "head_dim must be even for RoPE"
    half = dim // 2
    freq = torch.pow(10000, -(2 * torch.arange(half) / dim))
    pos = torch.arange(max_seq_len, dtype=freq.dtype).view(max_seq_len, 1)

    sin = torch.sin(pos * freq.view(1, half))[:seq_len].view(1, 1, seq_len, half)
    cos = torch.cos(pos * freq.view(1, half))[:seq_len].view(1, 1, seq_len, half)

    x1 = x[..., ::2]
    x2 = x[..., 1::2]
    y1 = cos * x1 - sin * x2
    y2 = sin * x1 + cos * x2
    y = torch.stack([y1, y2]).reshape_as(x)
    return y
