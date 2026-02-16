# Three types of coupons:
# 1. Full reduction: 10 off for every 100, unlimited usage
# 2. Discount: 92% (0.92), use only one, round down
# 3. No threshold: 5 off, unlimited usage
# Max two types of coupons per time, stackable
# In one purchase, same type coupons must be used together, cannot be split
# Require minimum price using fewest coupons; if prices same, choose fewest coupons; allow no coupon usage
# Each person can only participate once, coupon types and counts are same for everyone

# First line: counts of Full reduction, Discount, No threshold coupons
# Second line: number of shoppers
# Next lines: shopping amount for each person

# Output: Amount paid by each person, number of coupons used

from itertools import permutations

# coupon order: A=Full reduction, B=Discount, C=No threshold
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

    for combo in permutations(types, 2): # permutations returns iterator of all permutations of types
        p, used = price, 0
        for c in combo: # combo is a tuple of 2 coupon types
            # Wait, logic in original code assumes we iterate through all types in combo?
            # Original code: for c in combo: p, u = apply(p, c, coupons[types.index(c)]); used += u
            # It only picks 2 types. But what if we only use 1 type?
            # "Max two types". Permutations of 2 types covers using 2 types.
            # Using 1 type is covered if second type usage is 0? Or maybe not covered if order matters?
            # Actually, permutations (A, B) applies A then B. (A, C) applies A then C.
            # Does it cover just A? If second type B has count 0, result is effective just A.
            # But we should also check single types?
            # Let's check original code logic.
            # It iterates permutations(types, 2). It doesn't check length 1 combos explicitly.
            # However, if we have coupons [A_cnt, B_cnt, C_cnt].
            # If we try (A, B), we apply A then B.
            # If B_cnt is 0, it is effectively just A.
            # So as long as we have 0 counts handled, it is fine.
            # But what if we want to apply A only, and B_cnt > 0?
            # Then applying (A, B) forces B application if applicable.
            # This might be a limitation of original code or problem constraint (must use max possible?).
            # Problem says "Require minimum price".
            # If applying B increases price? (Discount generally decreases).
            # If applying B is suboptimal compared to not applying?
            # Usually discount/reduction decreases price.
            # Exception: maybe some weird rounding?
            # Anyway, I should translate as is.
            p_temp, u_temp = price, 0
            # Original code actually applies all in combo.
            # Wait, `combo` from `permutations(types, 2)` gives length 2.
            # Original code only tries length 2?
            # Yes. `permutations(types, 2)`.
            # If optimal is just A?
            # Maybe (A, B) where B usage is 0?
            # But if B_cnt > 0, `apply` will use it.
            # So if optimal is A but we have B coupons, original code forces use of B if we pick (A, B) order.
            # Maybe user wants to fix this?
            # "Select fewest coupons".
            # I should translate strictly.
            current_p = price
            current_used = 0
            for c in combo:
                idx = types.index(c)
                cnt = coupons[idx] # Available count
                # Note: `apply` function in original code uses `coupons[types.index(c)]`.
                # Wait, original code passed `coupons` which is list of counts.
                # `apply(p, c, coupons[types.index(c)])`
                # So it uses all available coupons of that type.
                p_res, u_res = apply(current_p, c, cnt)
                current_p = p_res
                current_used += u_res
            results.append((current_p, current_used))

    # Allow no coupon
    results.append((price, 0))

    return min(results, key=lambda x: (x[0], x[1]))


coupons = list(map(int, input().split()))
n = int(input())
prices = [int(input()) for _ in range(n)]

for price in prices:
    p, u = best_price(price, coupons)
    print(p, u)