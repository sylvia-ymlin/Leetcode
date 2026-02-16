# A pile of rectangular blocks, same cross-section, build a wall, same height each layer, max height?
# Input: List of block lengths, space separated
# Output: Max height

# Brute force
# First sum up
# Wall length must be at least max block length
# Or sum of max and min block length?
# Then it becomes a Two Sum problem, find a partner for each number so sum equals wall length
# If any number has no partner, return -1

from collections import Counter

def can_build(length, blocks, cnt) -> bool:
    """Check if blocks can build walls of layer length L"""
    # This logic seems to check if we can form pairs summing to `length`?
    # Or single blocks equal to `length`?
    # `blocks` iterates all blocks.
    # If block == length, continue (good layer).
    # If cnt[block] == 0, continue (already used).
    # elif cnt[block] > 0:
    #   complement = length - block
    #   if cnt[complement] == 0: return False (cannot form layer)
    #   else: decrement counts.
    # This greedy pairing might fail if `length` can be formed by >2 blocks?
    # Problem says "rectangular blocks... build a wall... every layer height same".
    # Wait, "same cross-section". So laying them side-by-side?
    # "Every layer height same"? Probably means "Every layer LENGTH same"?
    # Because they are blocks, maybe "height" of wall depends on how many layers.
    # If every layer has length L, max height = Total Sum / L.
    # The code checks `can_build` for `target_len`.
    # It tries to form layers of `target_len` using 1 or 2 blocks?
    # The code `if block == length: continue` and `complement = length - block` implies max 2 blocks per layer.
    # Is this a constraint of the problem?
    # "Stack blocks... max height".
    # If I have blocks 1, 1, 1 and target 3. Pairs: (1, ?). No.
    # But (1, 1, 1) could form 3.
    # The code only checks pairs.
    # Maybe problem constraint "at most 2 blocks per layer"?
    # Or "cylindrical blocks"?
    # Given the code, I will preserve the logic (Max 2 blocks per layer strategy).

    for block in blocks:
        if block == length:
            continue
        if cnt[block] == 0:
            continue
        elif cnt[block] > 0:
            complement = length - block
            if cnt[complement] == 0:
                return False
            else:
                cnt[block] -= 1
                cnt[complement] -= 1
    return True

blocks = list(map(int, input().split()))
total_length = sum(blocks)

max_len = max(blocks)
min_len = min(blocks)

cnt = Counter(blocks)
height = -1

# Try target length = max_len
if total_length % (max_len) == 0:
    target_len = max_len
    # Is valid?
    if can_build(target_len, blocks, cnt.copy()):
        height = total_length // target_len

# Only if failed, try target length = max_len + min_len
# Why only these two targets?
# If we want max height, we want min layer length.
# Min layer length >= max_block_len (must contain largest block).
# So `target_len = max_len` is the absolute best case.
# If that fails, maybe pairs? `max_len` + `min_len`?
# Why not `max_len` + something else?
# Maybe `max_len` must be paired with `min_len` to have any chance if `max_len` alone doesn't work?
# This logic seems potentially incomplete but I will stick to translation.
if height == -1 and total_length % (max_len + min_len) == 0:
    target_len = max_len + min_len
    if can_build(target_len, blocks, cnt.copy()):
        height = total_length // target_len

print(height)