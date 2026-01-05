# 返回取 x 元 零食可以达到的最大喜欢度

# x ： 总价格； N ： 零食种类数
x, N = map(int, input().split())
# 零食价格，数量，喜欢程度
snacks = []
for _ in range(N):
    price, quantity, like = map(int, input().split())
    snacks.append((price, quantity, like))

# dp[i]: 价格为 i 时，最大喜欢度
# 动态规划 - 多重背包
# 为加速计算，可以拆为 0-1 背包问题
goods = []
for price, quantity, like in snacks:
    for k in range(1, quantity + 1):
        goods.append((price * k, like * k))

dp = [0] * (x + 1)

# 每样物品，选或不选
for price, like in goods:
    for j in range(x, price - 1, -1):
        dp[j] = max(dp[j], dp[j - price] + like)

print(dp[x])

# 时间复杂度：O(x * sum(quantity)) # 外层遍历所有物品，内层遍历价格
# 空间复杂度：O(max(x, sum(quantity))) # 物品个数 和 dp 数组 取大