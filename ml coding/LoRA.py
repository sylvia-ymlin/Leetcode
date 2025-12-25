# B matrix should be initialized as zeros to ensuer the initial LoRA module is identity mapping, having no effect on the pre-trained model.
from torch import nn
import torch

class LoRA_Linear(nn.Module):
    def __init__(self, linear, r, alpha):
        # linear: pre-trained linear layer
        super().__init__()
        self.linear = linear
        self.r = r
        self.alpha = alpha

        if r > 0:
            self.lora_A = nn.Parameter(torch.randn(linear.in_features, r))
            # initialize weights
            nn.init.kaiming_normal_(self.lora_A)
            self.lora_B = nn.Parameter(torch.zeros(r, linear.out_features))
        else:
            self.lora_A = None
            self.lora_B = None
    
    def forward(self, x):
        if self.r == 0:
            return self.linear(x)
        else:
            return self.linear(x) + x @self.lora_A @ self.lora_B * (self.alpha / self.r)
