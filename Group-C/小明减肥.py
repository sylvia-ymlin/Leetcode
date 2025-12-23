# 从数组中选出 k 个数和为 t
# 输出有多少种选法

# 输入格式
# n t k
# a1 a2 ... an

# 动态规划，选或不选，选够 k 个 且和为 t，得到一个可行解
def dfs(start: int, rem_k: int, cur_sum: int) -> int:
    # 没有物品可选了
    if start == n:
        return 0
    
    # 选了足够多件
    if rem_k == 0:
        return 1 if cur_sum == t else 0
    
    # 超出背包容量或剩下的物品我不够选
    if cur_sum > t or rem_k > n - start:
        return 0
    
    # 不选当前物品
    count = dfs(start + 1, rem_k, cur_sum)
    # 选当前物品
    count += dfs(start + 1, rem_k - 1, cur_sum + nums[start])

    return count

# 读入数据
n, t, k = map(int, input().split())
nums = list(map(int, input().split()))

# 验证输入
if not(0 < n < 10 and t > 0 and 0 < k <= n):
    print(0)
    exit()

if any(num <= 0 for num in nums):
    print(0)
    exit()

print(dfs(0, k, 0))
