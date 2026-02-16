# Neural Network Model Compression based on Pruning
# Given input matrix x, weight matrix w, pruning ratio ratio
# Perform structured pruning on W, use pruned results to calculate model prediction

# X: n x d, n is sample count, d is feature count
# W: d x c, c is class count
# Calculation process:
# h = X * W
# s = softmax(h)
# Output class is argmax(s)

# Pruning
# Prune W by row, pruning ratio ratio, pruning metric L1 norm (sum of absolute values of row vector)

# Pruning definition
# 1. Row pruning: remove unimportant rows, keep important rows
# 2. Physical meaning: remove feature inputs with less impact on output, to compress model input dimension
# 3. After pruning
# - w: (d-k) x c, k is number of pruned rows
# - x: n x (d-k)
# Pruning metric: calculate sum(abs(w[i])), choose ratio% rows with smallest sum to prune, remove corresponding columns in x

# k = ratio * d rounded down

n, d, c = map(int, input().strip().split())

X = [list(map(float, input().strip().split())) for _ in range(n)]
W = [list(map(float, input().strip().split())) for _ in range(d)]
ratio = float(input().strip())

k = int(d * ratio)
if k == 0 and ratio > 0:
    k = 1 # at least prune one row

# Calculate L1 norm for each row
l1_norms = [(i, sum(abs(W[i][j]) for j in range(c))) for i in range(d)]
# Sort by L1 norm, choose top k to prune
l1_norms.sort(key=lambda x: x[1])

# No need for explicit pruning, just skip calculation for pruned rows
h = [[0.0] * c for _ in range(n)] # x * w
pruned_indices = set(idx for idx, _ in l1_norms[:k])
for i in range(n):
    for j in range(d):
        if j in pruned_indices:
            continue
        for col in range(c):
            h[i][col] += X[i][j] * W[j][col]
            
# Calculate softmax
import math
s = [[0.0] * c for _ in range(n)]
for i in range(n):
    max_h = max(h[i])
    exp_sum = sum(math.exp(h[i][j] - max_h) for j in range(c))
    for j in range(c):
        s[i][j] = math.exp(h[i][j] - max_h) / exp_sum

# Output classes
labels = []
for i in range(n):
    predicted_class = s[i].index(max(s[i]))
    labels.append(predicted_class)

print(' '.join(map(str, labels)))
