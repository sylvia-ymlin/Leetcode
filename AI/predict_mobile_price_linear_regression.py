# Three features, build linear regression model, predict mobile phone price
# Require normal equation implementation

# First line: sample size
# Second line: feature1, feature2, feature3, price (groups of 4)
# Third line: feature1, feature2, feature3, require predicted price (groups of 3)
# Output predicted price, rounded to integer

# Read data
n = int(input())

data = list(map(int, input().split()))

m = int(input()) # Number of test data groups

tests = list(map(int, input().split()))

train_X = []
train_Y = []
for i in range(n):
    x1 = data[4 * i]
    x2 = data[4 * i + 1]
    x3 = data[4 * i + 2]
    y = data[4 * i + 3]
    train_X.append([1, x1, x2, x3])  # Add bias term
    train_Y.append(y)

# Construct matrix form of normal equation
# X^T * X * W = X^T * Y

# Calculate X^T * X
XT_X = [[0] * 4 for _ in range(4)]
for i in range(n):
    for j in range(4):
        for k in range(4):
            XT_X[j][k] += train_X[i][j] * train_X[i][k]

# Calculate X^T * Y
XT_Y = [0] * 4
for i in range(n):
    for j in range(4):
        XT_Y[j] += train_X[i][j] * train_Y[i]

# Solve linear equation XT_X * W = XT_Y
# Use Gaussian elimination
def gaussian_elimination(A, b):
    n = len(b)
    for i in range(n):
        # Find pivot
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        # Elimination
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            b[k] -= factor * b[i]

    # Back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    return x

weights = gaussian_elimination(XT_X, XT_Y)
# Predict test data
res = []

for i in range(m):
    x1 = tests[3 * i]
    x2 = tests[3 * i + 1]
    x3 = tests[3 * i + 2]
    y_pred = weights[0] + weights[1] * x1 + weights[2] * x2 + weights[3] * x3
    res.append(str(round(y_pred)))

print(' '.join(res))
