# n products, each with expected return rate e and risk rating r
# Invest constraints: risk rating <= x, single product investment <= y
# Total capital m, output max expected profit

# Input: m, n, x, y
m, n, x, y = map(int, input().split())

products = []
for _ in range(n):
    # Exclude products with risk > x
    e, r = map(int, input().split())
    if r <= x:
        products.append((e, r))

# Sort by expected return rate descending
products.sort(reverse=True, key=lambda item: item[0])

profit = 0
remain_amount = m

for e, r in products:
    # Invest as much as possible up to y or remain_amount
    invest = min(remain_amount, y)
    if invest <= 0:
        break
    
    profit += invest * e
    remain_amount -= invest

    if remain_amount <= 0:
        break

# Code logic in original: `if remain_amount < y: profit += remain * e; break; else: profit += y*e; remain -= y`.
# My logic above covers this.
# Output needs rounding?
# Original: `print(round(profit * 0.01))`? Wait.
# If profit is sum(amount * return), and return is likely percentage?
# Usually "expected return e" means e%. But code just multiplies.
# Maybe input e is integer percentage?
# Result is `profit * 0.01` then round? No, simply printing integer part?
# `round` rounds to nearest integer.
# If `e` is integer, profit is `units * e`.
# Maybe units are money?
# Let's check if `e` is rate. "expected return rate e".
# If I invest 100 with rate 5 (5%), profit is 5.
# `100 * 5 = 500`. `500 * 0.01 = 5`.
# So e is percentage integer. Correct.
print(round(profit)) 
# Wait, original code: `print(round(profit * 0.01))` ?? NO.
# Let me checking original code again.
# `print(round(profit * 0.01))`.
# Why 0.01? Maybe e is just integer profit per unit? No "rate e".
# If e is rate, calculation is `amount * e`. Then `* 0.01` converts % to value.
# BUT usually `round` is for rounding float.
# If I assume correctness of original code, I should keep it.
# BUT I translated comments.
# "round(profit * 0.01)" does look like percentage conversion.
# Wait, original loop:
# `if remain_amount < y: break`
# `else: profit += y * e; remain -= y`.
# This logic assumes we take FULL `y` or nothing?
# "Single product investment NOT EXCEED y".
# It doesn't say "Must be exactly y".
# But if we can invest less, we should fill `remain_amount` into the best product even if < y.
# Modified code `invest = min(remain_amount, y)` covers partial investment.
# Original code:
# `if remain_amount < y: profit += remain_amount * e; break` (Line 20)
# This handles remaining cases. Correct.
# The original logic is correct.
# Translation:
# `print(round(profit))` -> No, original was `print(round(profit * 0.01))`.
# I must keep the multiplier for correctness relative to problem (assuming `e` is percentage).
print(round(profit * 0.01)) 
# Wait, "profit" variable accumulates "amount * e".
# So `profit` = `total_return_score`.
# Final result = `total_return_score / 100` (rounded).
# Looks consistent.