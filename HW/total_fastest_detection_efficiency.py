# Clarify problem statement
# Input: Number of samplers, Number of volunteers
# Second line: Efficiency of each sampler (N/h)
# Output: Fastest total detection efficiency

# Sampler efficiency fluctuation rule:
# If no volunteer, efficiency = N - N*0.1*2 -> 0.8 N
# With 1 volunteer? (Code logic: k=0 -> 0.8N; k<=4 -> N + (k-1)*0.1N?)
# Let's check `eff` function:
# k=0: return N - 2 * (N // 10)  => N - 0.2N = 0.8N
# k.e.g 1: return N + 0 = N
# k=2: return N + 1 * (N // 10) = 1.1N
# k=3: return N + 2 * (N // 10) = 1.2N
# k=4: return N + 3 * (N // 10) = 1.3N
# k>4: return N + 3 * (N // 10) = 1.3N (No more increase)
# So max effective volunteers per sampler is 4.

def eff(N, k):
    if k == 0:
        return N - 2 * (N // 10)   # 0.8N
    if k <= 4:
        return N + (k - 1) * (N // 10)
    return N + 3 * (N // 10)

# Read input
n, m = map(int, input().split())
efficiencies = list(map(int, input().split()))

# dp[i][j] means max efficiency using first i samplers with j volunteers total
dp = [[0] * (m + 1) for _ in range(n + 1)]

# Initialize: when 0 volunteers used (impossible if m>0? No, j represents total used)
# Base case: first i samplers with 0 volunteers
# Logic in code: `dp[i][0] = dp[i-1][0] + eff(efficiencies[i-1], 0)`
# This initializes column 0. Correct.

for i in range(1, n + 1):
    dp[i][0] = dp[i-1][0] + eff(efficiencies[i-1], 0)

# Init row 0? dp[0][j] is 0 (0 samplers -> 0 efficiency). Correct.

# Fill DP table
for i in range(1, n + 1): # Iterate samplers
    for j in range(1, m + 1): # Iterate total volunteers available
        # Try assigning k volunteers to current sampler i
        # k can be from 0 to min(4, j) ? 
        # Actually max beneficial is 4. Only need to try 0..4?
        # But if we have abundant volunteers, we might assign > 4? 
        # But efficiency doesn't increase after 4. So assigning 5 is same efficiency as 4 but costs more.
        # Since we want MAX efficiency with FIXED total volunteers m.
        # Wasting volunteers is suboptimal if they could be used elsewhere.
        # But if we have leftover, assigning > 4 is fine (efficiency same).
        # However, DP state `dp[i][j]` means *exactly* j volunteers used?
        # If so, we can iterate k from 0 to j.
        # But optimization: only need to try useful k (0..4).
        # What if j > 4 * i? Then some volunteers must be wasted.
        # The loop `for k in range(0, min(4, j) + 1)` only checks up to 4.
        # This implies we assume optimal solution never assigns > 4?
        # True, because shifting extra to another sampler is better or same.
        # BUT if ALL samplers have >4, then we just have extras.
        # The question asks for efficiency with `m` volunteers.
        # If m is very large, does it mean we MUST use all m?
        # Usually "equipped with m volunteers".
        # If we use less than m and get result X.
        # If we use m (by dumping extras), result is still X (since >4 gives same).
        # So efficiency is non-decreasing with volunteers.
        # The DP calculation `dp[n][m]` requires exactly m usage?
        # Loop `range(0, min(4, j) + 1)`:
        # dp[i][j] = max(dp[i-1][j-k] + eff(i, k)).
        # If we only check k up to 4, and j is large (e.g. 100 with 1 sampler),
        # dp[1][100] tries k=0..4.
        # dp[0][100], dp[0][99]... are all 0.
        # So dp[1][100] = 0 + eff(1, 4) (max).
        # This logic is correct for "at most m volunteers" or "exactly m"?
        # Since efficiency saturates, max efficiency with m is same as with min(m, 4*n).
        # The code logic `min(4, j)` limits k.
        # If j > 4, we use k=4, remaining j-4 must come from `dp[i-1]`.
        # If i=1, dp[0][any] is 0.
        # So dp[1][5] = dp[0][1] + eff(4) = 0 + eff(4).
        # So it correctly handles "dumping" extras implicitly by relying on previous states having handled their share.
        # Wait. `dp[i-1][j-k]`.
        # For i=1, j=5. k=0..4.
        # k=4: dp[0][1] + eff(4).
        # dp[0][1] is 0.
        # So it works.
        # It seems correct.

        for k in range(0, min(4, j) + 1): 
            dp[i][j] = max(
                dp[i][j], 
                dp[i-1][j-k] + eff(efficiencies[i-1], k))

# Output result
print(dp[n][m])