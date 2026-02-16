# Given total budget and number of component types, calculate max reliability of equipment within budget
# Given N components, select one from each type to assemble equipment, total budget within budget, maximize equipment reliability

# Dynamic programming, state transition from budget and component types dimensions
# dp[i][b] = Max reliability using first i types of components within budget b
# Equipment reliability is determined by the lowest reliability among selected components

budget, n = map(int, input().split())
m = int(input())
components = [[] for _ in range(n)]
for _ in range(m):
    t, c, r = map(int, input().split())
    components[t].append((c, r))

# dp = [[-1]*(budget+1) for _ in range(n+1)] # Initialize dp array, -1 means unreachable
# for b in range(budget+1):
#     dp[0][b] = float('inf')  # No component selected, reliability infinity

# for i in range(1, n+1):
#     for b in range(budget+1):
#         max_rel = -1
#         for rel, cost in components[i-1]:
#             if b >= cost and dp[i-1][b-cost] != -1:
#                 max_rel = max(max_rel, min(dp[i-1][b-cost], rel))
#         dp[i][b] = max_rel

# result = max(dp[n])
# print(result)

# Optimize space complexity, use 1D array, depends only on previous row, update from back to front
dp = [float('inf')] * (budget + 1)
# Traverse each component type
for i in range(n):
    new_dp = [-1] * (budget + 1)
    for b in range(budget + 1):
        for rel, cost in components[i]:
            if b + cost <= budget:
                new_dp[b + cost] = max(new_dp[b + cost], min(dp[b], rel))
    dp = new_dp

result = max(dp)
print(result)
