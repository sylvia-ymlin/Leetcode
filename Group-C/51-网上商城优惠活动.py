# 三种优惠券：
# 满减：满100 减 10, 不限使用张数
# 打折: 92 折, 只能使用一张，向下取整
# 无门槛 ：立减 5 元, 不限使用张数
# 每次最多使用两种优惠券，可叠加
# 一次购物中，同类优惠券必须一次使用，不能交替分开
# 要求使用最少优惠券获得最低价格；同等优惠价格，选择优惠券使用最少的方案；可以允许某次购物不使用优惠券
# 优惠活动每个人只能参加一次，每个人的优惠券种类和数量一致

# 第一行：满减、打折、无门槛 三种优惠券的数量
# 第二行，购物人数
# 接下来每行：每个人的购物金额

# 输出：每个人支付的金额，使用的优惠券的数量

from itertools import permutations

# coupon order: A=满减, B=打折, C=无门槛
def apply(price, coupon, cnt):
    if coupon == 'A':
        used = min(price // 100, cnt)
        return price - used * 10, used
    if coupon == 'B' and cnt > 0:
        return int(price * 0.92), 1
    if coupon == 'C':
        return price - 5 * cnt, cnt
    return price, 0


def best_price(price, coupons):
    types = ['A', 'B', 'C']
    results = []

    for combo in permutations(types, 2): # permutations 会对 types 中的元素进行全排列，返回一个迭代器
        p, used = price, 0
        for c in combo:
            p, u = apply(p, c, coupons[types.index(c)])
            used += u
        results.append((p, used))

    # 允许不使用优惠券
    results.append((price, 0))

    return min(results, key=lambda x: (x[0], x[1]))


coupons = list(map(int, input().split()))
n = int(input())
prices = [int(input()) for _ in range(n)]

for price in prices:
    p, u = best_price(price, coupons)
    print(p, u)