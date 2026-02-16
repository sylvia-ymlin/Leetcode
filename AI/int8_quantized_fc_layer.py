# Fully connected layer INT8 asymmetric quantization implementation
# Perform INT8 asymmetric quantization on input vector x and weight matrix W, calculate FC layer using quantized integer values x_q and W_q (bias not considered)
# Dequantize the quantized integers to get x_deq and W_deq, and perform FC layer calculation again
# Calculate Mean Squared Error (MSE) between the two results, output MSE*100000 rounded

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

# Input x
n = int(input())
x = list(map(float, input().split()))
# Input W
m, n = map(int, input().split())
W = [list(map(float, input().split())) for _ in range(m)]

# Quantization
x_q = quantize(x, min(x), max(x))
w_min = min(min(row) for row in W)
w_max = max(max(row) for row in W)
W_q = [quantize(row, w_min, w_max) for row in W]

# FC layer calculation (quantized)
y_q = []
for row in W_q:
    y_q.append(sum([row[i] * x_q[i] for i in range(n)]))

# Dequantization
x_deq = dequantize(x_q, min(x), max(x))
W_deq = [dequantize(row_q, w_min, w_max) for row_q in W_q]
# FC layer calculation (dequantized)
y_deq = []
for row in W_deq:
    y_deq.append(sum([row[i] * x_deq[i] for i in range(n)]))

# Original FC layer calculation (before quantization)
y = []
for row in W:
    y.append(sum([row[i] * x[i] for i in range(n)]))

# Calculate MSE
mse = mse_error(y, y_deq)

# First line outputs the quantized FC layer result
print(' '.join(map(str, y_q)))
# Second line outputs the MSE * 100000 rounded
print(round(mse * 100000))