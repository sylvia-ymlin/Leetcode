from torch import nn
import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F

# hyperparameters
bs = 63
lr = 1e-3
wd = 1e-4 # weight decay
epochs = 3

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

    def forward(self, x):
        assert x.shape[-1] == self.in_dim, f"x.shape[-1] should be {self.in_dim}, got {x.shape[-1]}"
        assert len(x.shape) == 2, f"x should be 2-D tensor, got {x.shape}"
        return self.layers(x)

model = MLP(28*28, 256, 10, num_layers=2).cuda()

tfm = transforms.ToTensor()
train_dataset = torchvision.datasets.MNIST("./", train=True, download=True, transform=tfm)
test_dataset = torchvision.datasets.MNIST("./", train=False, download=True, transform=tfm)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=bs, shuffle=True, num_workers=2, drop_last=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=bs, shuffle=False, num_workers=2, drop_last=False)

optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=wd)

# training loop
model.train()
for epoch in range(epochs):
    for i, batch in enumerate(train_loader):
        x, y = batch
        x, y = x.cuda(), y.cuda() # move to GPU
        # reshape input image to vector
        x = x.view(x.shape[0], -1)
        logits = model(x)
        loss = F.cross_entropy(logits, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if i % 100 == 0:
            print(f"epoch {epoch}, iter {i}, loss = {loss.item():.4f}")
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
