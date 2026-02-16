# Not that difficult!


# Quantization: to reduce memory usage and improve calculation efficiency, quantize floating point numbers to integers
# Example: int(W_float * 2^8) converts a float less than 1 to int8

# A set of [N, H] model weights, N is number of layers, H is neurons per layer
# Quantize network weights, require quantization bit Q_i to be consistent within each layer, but can be different between layers
# Quantization rule: W_q = int(W_float * 2^Q_i)
# Error measurement: e = |W_float - W_q / 2^Q_i|
# Requirement: sum(Q_i) <= Q_max
# Minimize total error, give optimal Q_i allocation scheme
# Q_i = {2, 4, 8}

# Essentially a variant of knapsack problem, solve using dynamic programming
# dp[i][j] represents min error for first i layers using j bits

# Read data
N, H, Q_max = map(int, input().split())
# Read network weights, N rows H columns
weights = [list(map(float, input().split())) for _ in range(N)]

dp = [[float('inf')] * (Q_max + 1) for _ in range(N + 1)]
# State transition equation
# dp[i][j] = min(dp[i-1][j - Q_k] + error_i(Q_k)) for Q_k in {2,4,8} if j >= Q_k
# Initialization
dp[0][0] = 0
quantization_bits = [2, 4, 8]
# Pre-calculate error for each layer under different quantization bits
errors = [[0] * len(quantization_bits) for _ in range(N)]
for i in range(N):
    for k, Q_k in enumerate(quantization_bits):
        error = 0
        for w in weights[i]:
            W_q = int(w * (1 << Q_k)) # According to requirement, direct int
            error += abs(w - W_q / (1 << Q_k))
        errors[i][k] = error

# Dynamic programming table filling
for i in range(1, N + 1):
    for j in range(Q_max + 1):
        for k, Q_k in enumerate(quantization_bits):
            if j >= Q_k:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - Q_k] + errors[i - 1][k])

# Output min error (x 100 and floor/truncate)
# Min error should be min of dp[N][0..Q_max]
print(int(min(dp[N]) * 100))
