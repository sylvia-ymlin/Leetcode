# Version number format: separated by dot
# Find the highest available version between two versions
# Find first different segment, calculate v2 - v1 + 1 (counts integers in between?)
# Problem: "Find max available version number between two...".
# Logic: `v2[i] - v1[i] - 1`.
# Constraint: Subsequent segments of v2 must be 0? `all(x==0 for x in v2[i+1:])`.
# This logic is very specific to a certain problem variant.
# Possibly "Calculate number of intermediate versions"?
# Or "Difference calculation"?
# Given code:
# Finds first index i where v1[i] != v2[i].
# Checks if all v2 after i are 0.
# If so, prints `v2[i] - v1[i] - 1`.
# Else prints 0.
# I will just translate comments and keep logic.

v1_str, v2_str = input().replace(',', ' ').split()
v1 = list(map(int, v1_str.split('.')))
v2 = list(map(int, v2_str.split('.')))

for i in range(min(len(v1), len(v2))):
    if v1[i] != v2[i]:
        # Logic: if first difference found, check if rest of v2 is all zeros
        # This seems to verify if v2 is a "major" version jump from v1?
        # e.g. v1=1.2.3, v2=2.0.0. i=0. diff. rest of v2 is .0.0. OK.
        # Print v2[0] - v1[0] - 1 = 2-1-1 = 0?
        # If v2=3.0.0. 3-1-1 = 1.
        # It counts valid versions strictly BETWEEN major versions?
        if all(x==0 for x in v2[i+1:]):
            print(v2[i] - v1[i] - 1)
            exit(0)
        else:
            # If not all zeros, condition failed?
            # Original code loop continues?
            # NO. `if v1!=v2 ... exit(0)`.
            # What if `if` is False (rest not zeros)?
            # Loop continues? But `v1[i] != v2[i]` was True.
            # So next iteration `i` increments.
            # But the *first* difference determines ordering usually.
            # If we skip it, we compare 2nd segments? (Compare 2 vs 0 in 1.2 vs 2.0?)
            # No, version comparison stops at first diff.
            # So presumably if condition fails, it should terminate or print 0?
            # Original code: `if ... print ... exit`. No `else` for inner if.
            # So if `all(zeros)` is false, it continues loop.
            # This implies looking for a *later* difference?
            # But if `v1[i] != v2[i]`, they are already different.
            # e.g. 1.1 vs 1.2. i=1. diff. rest empty or 0.
            # If 1.5 vs 1.2. i=1. diff.
            # The logic is weird but I will preserve it.
            pass

print(0)