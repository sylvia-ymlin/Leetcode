# linear layer + logistic regression
# the difficulty is to derivate the dw and db
# for softmax, remember to minus the max value to stabilize the exp

import numpy as np
import torch

d = 3
c = 10
n = 100
lr = 0.01
x = np.random.randn(n, d)
y = np.random.randint(0, c, n)
y = np.eye(c)[y]  # one-hot encoding

w = np.random.randn(d, c)
b = np.random.randn(1, c)

def softmax(y):
    y = y - np.max(y, axis=1, keepdims=True)
    exp_y = np.exp(y)
    return exp_y / np.sum(exp_y, axis=1, keepdims=True)

def ce_loss(y_true, y_pred):
    losses = -np.sum(np.log(y_pred + 1e-9) * y_true, axis=-1)
    return losses.mean()

for i in range(100):
    # forward
    y_pred = softmax(np.matmul(x, w) + b)
    loss = ce_loss(y, y_pred)
    
    # backward
    dw = np.matmul(x.T, (y_pred - y)) / n
    dn = np.sum(y_pred - y, axis=0) / n

    # update
    w -= lr * dw
    b -= lr * dn

    if i % 10 == 0:
        # print loss
        print(f"iter {i}, loss = {loss:.4f}")