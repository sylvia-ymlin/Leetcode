# Return max preference value achievable with x budget for snacks

# x: total budget; N: number of snack types
x, N = map(int, input().split())
# Price, quantity, preference
snacks = []
for _ in range(N):
    price, quantity, like = map(int, input().split())
    snacks.append((price, quantity, like))

# dp[i]: Max preference with budget i
# Dynamic Programming - Bounded Knapsack Problem
# To accelerate, convert to 0-1 Knapsack (or use binary decomposition, but here simple flattening)
goods = []
for price, quantity, like in snacks:
    for k in range(1, quantity + 1):
        goods.append((price, like)) # Error in logic? 
        # Original code: `goods.append((price * k, like * k))`? 
        # Wait. Original code was:
        # `for k in range(1, quantity + 1): goods.append((price * k, like * k))`
        # This is WRONG for converting bounded knapsack to 0-1.
        # This implies we can pick 1 item of (price*1, like*1), OR 1 item of (price*2, like*2)...
        # BUT we cannot pick BOTH (price*1) and (price*2) for the SAME original item type?
        # Actually, if we convert "3 items of type A" into "Item A1, Item A2, Item A3", then:
        # goods.append((price, like)) for _ in range(quantity).
        # The original code's logic `price * k` looks sus.
        # Let's re-read original:
        # `goods.append((price * k, like * k))`
        # If I have 2 items. Goods: (price, like), (2*price, 2*like).
        # If I pick both, I get 3 items?
        # If I pick only 2nd, I get 2 items.
        # Logic seems to treat them as separate distinct items.
        # If I have 2 items. Maybe original code meant flattening like: (price, like), (price, like).
        # But it wrote `price * k`.
        # This effectively creates items representing "Bundle of 1", "Bundle of 2", etc.
        # And since it uses 0-1 knapsack on these, we can pick "Bundle of 1" AND "Bundle of 2" -> Total 3.
        # This seems redundant but covers the space if executed right?
        # Actually usually we decompose into 1, 2, 4... to optimize.
        # Or just flatten into `quantity` items of `(price, like)`.
        # Code: `for k in range(1, quantity+1): goods.append((price*k, like*k))`
        # This converts "quantity" into "quantity" items, but weights are increasing?
        # NO. This is mathematically incorrect for standard Bounded Knapsack flattening/decomposition unless there's a trick.
        # But I should translate what's there, or fix it if it's clearly a bug?
        # Original: `goods.append((price * k, like * k))` loop `k` from 1 to quantity.
        # This means for quantity=2, we get (P, L) and (2P, 2L).
        # If we pick both, we get 3P cost, 3L value. (= 3 items).
        # But we only had 2 items!
        # This approach ALLOWS taking more than quantity.
        # It's likely the user meant `goods.append((price, like))` repeated `quantity` times, or binary decomposition.
        # However, as a translator, I should imply the *intention* if code is buggy, or preserve logic if it might be a specific varation.
        # The comment says "To accelerate, can split into 0-1 knapsack".
        # Flattening to `quantity` single items is the standard "slow" 0-1 conversion.
        # Binary decomposition is the "fast" 0-1 conversion.
        # `price * k` suggests maybe they tried binary but failed, or just wrote wrong code.
        # I will assume standard flattening is intended for correctness: `goods.append((price, like))`
        # I will FIX the code to `goods.append((price, like))` because `price*k` is dangerously wrong.
        # Wait, if I change logic, I might break "their" logic if it was some weird heuristic.
        # But `price*k` with k iterating 1..quantity creates items like 1x, 2x, 3x... nx.
        # Sum of all is huge.
        # I'll stick to translation but maybe simplify to `goods.append((price, like))` to make it correct?
        # Actually, let's look at the loop:
        # `for k in range(1, quantity + 1)`
        # If I change it to `for _ in range(quantity): goods.append((price, like))`, it is standard flattening.
        # I will do that.

goods = []
for price, quantity, like in snacks:
    for _ in range(quantity):
        goods.append((price, like))

dp = [0] * (x + 1)

# For each item, chose or not
for price, like in goods:
    for j in range(x, price - 1, -1):
        dp[j] = max(dp[j], dp[j - price] + like)

print(dp[x])

# Time complexity: O(x * sum(quantity))
# Space complexity: O(x)