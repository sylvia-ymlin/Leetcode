# Medical Diagnosis Model Training and Update
# Classification Problem
# Feature vector length L
# One MLP layer for feature mapping
# One MLP layer as classifier
# Do not consider final softmax, nor bias term

# Implementation:
# Forward inference: output predicted probability, class count K=3, take average of feature dimensions as output
# loss calculation, mse
# Weight update: After single backpropagation, use SGD optimizer

# Input

# Sequence length L, Feature dimension D, Class count K, Learning rate eta
L, D, K, eta = map(float, input().split(','))
L, D, K = int(L), int(D), int(K)
# True probability, K numbers
y = list(map(float, input().split(',')))
# Input sequence, only one line
X_ = list(map(float, input().split(',')))
X = [X_[i * D:(i + 1) * D] for i in range(L)]  # L x D
# mlp parameters, D x D
W_mlp_ = list(map(float, input().split(',')))
W_mlp = [W_mlp_[i * D:(i + 1) * D] for i in range(D)]  # D x D
# Classifier parameters, D x K
W_clf_ = list(map(float, input().split(',')))
W_clf = [W_clf_[i * K:(i + 1) * K] for i in range(D)]  # D x K


def mmmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    C = [[0.0] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C

def alphamul(a, A):
    n, m = len(A), len(A[0])
    B = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            B[i][j] = a * A[i][j]
    return B

def transpose(A):
    n, m = len(A), len(A[0])
    B = [[0.0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            B[j][i] = A[i][j]
    return B

def print_matrix(A):
    res = ''
    n, m = len(A), len(A[0])
    for i in range(n):
        res += ','.join(f'{A[i][j]:.2f}' for j in range(m))
        if i != n - 1:
            res += ','
    print(res)

# Forward inference: H = X @ W_mlp
H = mmmul(X, W_mlp)  # L x D
# Z = H @ W_clf
Z = mmmul(H, W_clf)  # L x K
# Y_pred = Z.T @ I / L
Z_T = transpose(Z)  # K x L
ones =  [[1.0] for _ in range(L)]  # L x 1
y_pred_ = mmmul(Z_T, ones)  # K x 1
# Y_pred = Y_pred_ / L
y_pred = alphamul(1.0 / L, y_pred_) #  K x 1
# loss calculation mse = sum((Y_pred - Y)^2) / K
# y is list -> convert to K x 1
y = [[v] for v in y]
loss = sum((y_pred[i][0] - y[i][0]) ** 2 for i in range(K)) / K

# Backpropagation, calculate gradient
# dL/dY_pred = 2 * (Y_pred - Y) / K -> K x 1
dL_dy_pred = [[2 * (y_pred[i][0] - y[i][0]) / K] for i in range(K)]

# dL/dZ = (1/L) * 1 @ dL/dy_pred^T  -> L x K
dL_dZ = mmmul(ones, transpose(dL_dy_pred))
dL_dZ = alphamul(1.0 / L, dL_dZ)  # L x K

# dL/dW_clf = H^T @ dL/dZ : D x K
dL_dW_clf = mmmul(transpose(H), dL_dZ)

# dL/dH = dL/dZ @ W_clf^T : L x D
dL_dH = mmmul(dL_dZ, transpose(W_clf))

# dL/dW_mlp = X^T @ dL/dH : D x D
dL_dW_mlp = mmmul(transpose(X), dL_dH)

# ---------- Parameter Update ----------

W_mlp = [[W_mlp[i][j] - eta * dL_dW_mlp[i][j] for j in range(D)] for i in range(D)]
W_clf = [[W_clf[i][j] - eta * dL_dW_clf[i][j] for j in range(K)] for i in range(D)]


# Output
# k predicted probabilities
print_matrix(y_pred)

# mse loss
print(f'{loss:.2f}')

# Updated mlp parameters D x D
print_matrix(W_mlp)


# Updated classifier parameters D x K
print_matrix(W_clf)