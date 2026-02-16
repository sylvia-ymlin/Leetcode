# Convolution Operation
# Implement Multi-channel Convolution Operation

# Input
# Input tensor shape c, H_in, W_in
# Convolution kernel shape c, kH, kW
# Stride

# padding is 0
# Skip if remaining size is smaller than kernel
# Calculate sum channel-wise

c, H_in, W_in = map(int, input().split())
X = []
for _ in range(c):
    mat = [list(map(int, input().split())) for _ in range(H_in)]
    X.append(mat)  # c x H_in x W_in

c, kH, kW = map(int, input().split())
K = []
for _ in range(c):
    mat = [list(map(int, input().split())) for _ in range(kH)]
    K.append(mat)  # c x kH x kW

stride, padding = map(int, input().split())

# Calculate output size
H_out = (H_in + 2 * padding - kH) // stride + 1
W_out = (W_in + 2 * padding - kW) // stride + 1

# Padding operation
X_pad = [[[0] * (W_in + 2 * padding) for _ in range(H_in + 2 * padding)] for _ in range(c)]
for ch in range(c):
    for i in range(H_in):
        for j in range(W_in):
            X_pad[ch][i + padding][j + padding] = X[ch][i][j]
X = X_pad

# Calculation
output = [[0.0] * W_out for _ in range(H_out)]
for i in range(H_out):
    for j in range(W_out):
        conv_sum = 0.0
        for ch in range(c): # Channel traversal
            for ki in range(kH):
                for kj in range(kW):
                    x_i = i * stride + ki
                    x_j = j * stride + kj
                    conv_sum += X[ch][x_i][x_j] * K[ch][ki][kj]
        
        output[i][j] = conv_sum

# Output result
for row in output:
    print(' '.join(str(int(x))for x in row))
