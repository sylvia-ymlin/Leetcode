from torch import nn

class MLP(nn.Module):
    def __init__(self,
        in_dim,
        hidden_dim,
        out_dim,
        *,
        num_layers=2):
        super().__init__() # initialize parent class nn.Module
        layers = []
        self.in_dim = in_dim
        # define hidden layers
        for _ in range(num_layers - 1):
            layers.append(nn.Linear(in_dim, hidden_dim))
            layers.append(nn.ReLU())
            in_dim = hidden_dim
        # define output layer
        layers.append(nn.Linear(in_dim, out_dim))
        self.layers = nn.Sequential(*layers) # the name of the attribute must be "layers"

model.eval()
# should know whole to calculate the accuracy
corret = 0
total = 0

with torch.no_grad():
    for batch in test_loader:
        x, y = batch
        x, y = x.cuda(), y.cuda() # move to GPU
        # reshape input image to vector
        x = x.view(x.shape[0], -1)
        logits = model(x)
        pred = torch.argmax(logits, dim=-1)
        corret += (pred == y).sum().item()
        total += y.shape[0]

print(f"acc = {corret / total:.4f}")
