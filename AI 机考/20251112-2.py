# 全连接层INT8非对称量化实现
# 对输入向量 x 和权重矩阵 W 执行 INT8 非对称量化，量化后的整数值 x_q 和 W_q 进行全连接层计算（不考虑偏置）
# 对量化后的整数反量化，得到 x_deq 和 W_deq，再次进行全连接层计算
# 计算两次结果后的均方误差（MSE），输出 MSEx100000 并四舍五入

def nearnest_round(x):
    if x - int(x) < 0.5:
        return int(x)
    elif x - int(x) > 0.5:
        return int(x) + 1
    else:
        return  2 * int((x + 1) / 2)

def clamp(t, lo, hi):
    if t < lo:
        return lo
    elif t > hi:
        return hi
    else:
        return t
    
def quantize(arr, min_val, max_val):
    scale = (max_val - min_val) / 255
    if scale == 0:
        return [-128 for _ in arr]
    return [clamp(nearnest_round((v - min_val)/scale) - 128, -128, 127) for v in arr]

def dequantize(arr_q, min_val, max_val):
    scale = (max_val - min_val) / 255
    if scale == 0:
        return [min_val for _ in arr_q]
    return [(v_q + 128) * scale + min_val for v_q in arr_q]

def mse_error(arr1, arr2):
    return sum((a - b) ** 2 for a, b in zip(arr1, arr2)) / len(arr1)

# 输入 x
n = int(input())
x = list(map(float, input().split()))
# 输入 W
m, n = map(int, input().split())
W = [list(map(float, input().split())) for _ in range(m)]

# 量化
x_q = quantize(x, min(x), max(x))
w_min = min(min(row) for row in W)
w_max = max(max(row) for row in W)
W_q = [quantize(row, w_min, w_max) for row in W]

# 全连接层计算（量化后）
y_q = []
for row in W_q:
    y_q.append(sum([row[i] * x_q[i] for i in range(n)]))

# 反量化
x_deq = dequantize(x_q, min(x), max(x))
W_deq = [dequantize(row_q, w_min, w_max) for row_q in W_q]
# 全连接层计算（反量化后）
y_deq = []
for row in W_deq:
    y_deq.append(sum([row[i] * x_deq[i] for i in range(n)]))

# 原始全连接层计算（量化前）
y = []
for row in W:
    y.append(sum([row[i] * x[i] for i in range(n)]))

# 计算均方误差
mse = mse_error(y, y_deq)

# 第一行输出量化计算的全连接层结果
print(' '.join(map(str, y_q)))
# 第二行输出 msex100000 并四舍五入后的结果
print(round(mse * 100000))