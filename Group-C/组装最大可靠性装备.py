# 给出总预算和元器件种类数，计算在预算范围内，设备的最大可靠性
# 给出 N 个元器件，从每个类型元器件中选择一个，组成设备，总预算在 budget 以内，最大化设备的可靠性

# 动态规划，从预算和元器件种类数两个维度进行状态转移
# dp[i][b] = 用前 i 类元件，在预算 b 内能获得的最大可靠性
# 设备的可靠性由所选元件中可靠性最低的决定

budget, n = map(int, input().split())
m = int(input())
components = [[] for _ in range(n)]
for _ in range(m):
    t, c, r = map(int, input().split())
    components[t].append((c, r))

# dp = [[-1]*(budget+1) for _ in range(n+1)] # 初始化 dp 数组，-1 表示不可达
# for b in range(budget+1):
#     dp[0][b] = float('inf')  # 没选任何元件，可靠性无穷大

# for i in range(1, n+1):
#     for b in range(budget+1):
#         max_rel = -1
#         for rel, cost in components[i-1]:
#             if b >= cost and dp[i-1][b-cost] != -1:
#                 max_rel = max(max_rel, min(dp[i-1][b-cost], rel))
#         dp[i][b] = max_rel

# result = max(dp[n])
# print(result)

# 优化空间复杂度，只用一维数组，只依赖于上一行的数据，从后向前更新
dp = [float('inf')] * (budget + 1)
# 遍历每一类元器件
for i in range(n):
    new_dp = [-1] * (budget + 1)
    for b in range(budget + 1):
        for rel, cost in components[i]:
            if b + cost <= budget:
                new_dp[b + cost] = max(new_dp[b + cost], min(dp[b], rel))
    dp = new_dp

result = max(dp)
print(result)

