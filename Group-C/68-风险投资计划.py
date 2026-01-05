# 有 n 中产品，每种给出 预期收益率 e 和 风险等级 r
# 要求投资产品的风险等级不超过 x，耽搁产品投资金额不超过 y
# 总投资金额 m，输出最大预期收益

m, n, x, y = map(int, input().split())
# 每种产品的收益和风险
products = []
for _ in range(n):
    # 首先可以直接排除风险等级超过 x 的产品
    e, r = map(int, input().split())
    if r <= x:
        products.append((e, r))

 # 直接排序，从投资收益高的开始投资
products.sort(reverse=True, key=lambda item: item[0])
profit = 0
remain_amount = m
for e, r in products:
    if remain_amount < y:
        profit += remain_amount * e
        break
    else:
        profit += y * e
        remain_amount -= y

print(round(profit * 0.01))