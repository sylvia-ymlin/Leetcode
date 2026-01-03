# 卷积操作
# 实现 多通道卷积操作

# 输入
# 形状为 c, H_in, W_in 的输入张量
# 形状为 c, kH, kW 的卷积核
# 步长 stride

# padding 为 0
# 剩余尺寸如果小于卷积核，跳过
# 逐通道计算求和

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

# 计算输出尺寸
H_out = (H_in + 2 * padding - kH) // stride + 1
W_out = (W_in + 2 * padding - kW) // stride + 1

# padding 操作
X_pad = [[[0] * (W_in + 2 * padding) for _ in range(H_in + 2 * padding)] for _ in range(c)]
for ch in range(c):
    for i in range(H_in):
        for j in range(W_in):
            X_pad[ch][i + padding][j + padding] = X[ch][i][j]
X = X_pad

# 计算
output = [[0.0] * W_out for _ in range(H_out)]
for i in range(H_out):
    for j in range(W_out):
        conv_sum = 0.0
        for ch in range(c): # 通道遍历
            for ki in range(kH):
                for kj in range(kW):
                    x_i = i * stride + ki
                    x_j = j * stride + kj
                    conv_sum += X[ch][x_i][x_j] * K[ch][ki][kj]
        
        output[i][j] = conv_sum

# 输出结果
for row in output:
    print(' '.join(str(int(x))for x in row))
