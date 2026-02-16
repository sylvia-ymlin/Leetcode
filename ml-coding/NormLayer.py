# LayerNorm: only for feature dim, per sample, per token normalization

class LayerNorm(nn.Module):
    def __init__(self, dim, eps=1e-5):
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(dim)) # scale
        self.beta = nn.Parameter(torch.zeros(dim)) # shift
        self.eps = eps
    
    def forward(self, x):
        # x: [batch_size, seq_len, dim]
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, keepdim=True, unbiased=False)
        x_norm = (x - mean) / torch.sqrt(var + self.eps) # avoid div 0
        return self.gamma * x_norm + self.beta

# no centerizing, only scaling
class RMSNorm(nn.Module):
    def __init__(self, dim, eps=1e-8): # can use smaller eps
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(dim)) # scale
        self.eps = eps

    def forward(self, x):
        rms = torch.sqrt((x ** 2).mean(dim=-1, keepdim=True) + self.eps)
        x_norm = x / rms
        return self.gamma * x_norm

# BatchNorm: rarely used in NLP, more in CV
class BatchNorm(nn.Module):
    def __init__(self, dim, eps=1e-5, momentum=0.1):
        super().__init__()
        self.gamma = nn.Parameter(torch.ones(dim)) # scale
        self.beta = nn.Parameter(torch.zeros(dim)) # shift
        self.eps = eps
        self.momentum = momentum

        # running stats
        self.register_buffer('running_mean', torch.zeros(dim))
        self.register_buffer('running_var', torch.ones(dim))
    
    def forward(self, x):
        if self.training:
            mean = x.mean(dim=(0,1)) # over batch and seq_len
            var = x.var(dim=(0,1), unbiased=False)

            # update running stats
            self.running_mean = (1 - self.momentum) * self.running_mean + self.momentum * mean
            self.running_var = (1 - self.momentum) * self.running_var + self.momentum * var
        else: # for testing, use running stats
            mean = self.running_mean
            var = self.running_var
        
        x_norm = (x - mean) / torch.sqrt(var + self.eps)
        return self.gamma * x_norm + self.beta