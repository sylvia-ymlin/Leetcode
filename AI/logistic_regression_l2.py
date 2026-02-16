import math

# sigmoid function
def sigmoid(z): # Numerically stable implementation
    if z >= 0:
        ez = math.exp(-z)
        return 1 / (1.0 + ez)
    else:
        ez = math.exp(z)
        return ez / (1.0 + ez)


# Calculate loss and gradient
def compute_loss_and_gradient(X, y, w, b, lam):
    n = len(y) # Sample size
    d = len(w) # Feature count

    eps = 1e-15 # Prevent log(0)

    loss = 0.0
    grad_w = [0.0] * d
    grad_b = 0.0

    # Calculate cross entropy and gradient
    for i in range(n):
        z = b 
        for j in range(d):
            z += w[j] * X[i][j]
        p = sigmoid(z) # Predicted probability
        yi = y[i]
        # Cross entropy
        loss += - (yi * math.log(p + eps) + (1 - yi) * math.log(1 - p + eps))
        # Gradient
        # dy_dz = hat_y - y
        diff = p - yi
        for j in range(d):
            grad_w[j] += diff * X[i][j] # Gradient for w
        grad_b += diff # Gradient for b
    
    # Average
    loss /= n
    for j in range(d):
        grad_w[j] /= n
    grad_b /= n

    # Add regularization constraint, after calculating loss and gradient
    l2 = 0.0
    for j in range(d):
        l2 += w[j] * w[j]
        grad_w[j] += lam / n * w[j] # L2 regularization gradient
    loss += (lam / (2 * n)) * l2 # L2 regularization loss
    return loss, grad_w, grad_b

def train(X, y, max_iters, alpha, lam, tol):
    n = len(y)
    d = len(X[0])

    # Initialize parameters
    w = [0.0] * d
    b = 0.0

    # Calculate loss once first
    loss, _, _ = compute_loss_and_gradient(X, y, w, b, lam)
    iter = 0
    while iter < max_iters and loss >tol:
        loss, grad_w, grad_b = compute_loss_and_gradient(X, y, w, b, lam)
        # Update parameters
        for j in range(d):
            w[j] -= alpha * grad_w[j]
        b -= alpha * grad_b

        iter += 1
    return w, b

def predict(X, w, b):
    d = len(w)
    z = b
    for j in range(d):
        z += w[j] * X[j]
    p = sigmoid(z)
    return 1 if p >= 0.5 else 0, p

# Input processing
n, max_iters, alpha, lam, tol = input().strip().split()
n = int(n)
max_iters = int(max_iters)
alpha = float(alpha)
lam = float(lam)
tol = float(tol)
X = []
y = []
for _ in range(n):
    line = list(map(float, input().strip().split()))
    X.append(line[:-1])
    y.append(int(line[-1]))

test_num = int(input().strip())
tests = []
for _ in range(test_num):
    line = list(map(float, input().strip().split()))
    tests.append(line)

# Train model
w, b = train(X, y, max_iters, alpha, lam, tol)
# Predict
for test in tests:
    pred, prob = predict(test, w, b)
    prob = round(prob, 4)
    print(pred, prob)
    # Different initialization may lead to slight differences from the answer
