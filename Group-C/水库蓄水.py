# 接雨水变体，只能有一个蓄水区间，求最大蓄水量及区间
# 思路：先做接雨水问题，计算每个位置蓄水后能够达到的最大高度

# 读入数据为list of int
height = list(map(int, input().split()))
n = len(height)

if n < 3:
    print(0)
    exit()

# 1. 预处理左右最大
left_max = [0] * n
right_max = [0] * n

for i in range(1, n):
    left_max[i] = max(left_max[i-1], height[i-1])

for i in range(n-2, -1, -1):
    right_max[i] = max(right_max[i+1], height[i+1])

# 2. 计算每个位置的蓄水量
water = [max(0, min(left_max[i], right_max[i]) - height[i]) for i in range(n)]

# 3. 找连续蓄水块的最大体积
best = 0
ans_l = ans_r = 0
i = 0

while i < n:
    if water[i] == 0:
        i += 1
        continue

    left = i
    current_volume = 0
    while i < n and water[i] > 0:
        current_volume += water[i]
        i += 1
    right = i - 1

    if current_volume > best or (current_volume == best and right - left < ans_r - ans_l):
        best = current_volume
        ans_l = left
        ans_r = right

# left 和 right 记录的是有蓄水的两端，输出的时候需要调整为包含边界的区间
if best == 0:
    print(0)
else:
    print(f"{ans_l - 1} {ans_r + 1}:{best}")