import sys
from ast import literal_eval
from collections import deque

def max_pruned_subtree(arr): # Complete binary tree represented by array

    n = len(arr) # Number of nodes
    if n == 0:
        return [] # Empty tree returns empty list

    # Mark whether each position is a real node (not None)
    valid = [x is not None for x in arr] # true or false

    # dp[i]: Max subtree sum rooted at i, allowing pruning subtrees with non-positive contribution
    dp = [0] * n # Initialize dp array, store max subtree sum for each node

    best_sum = None  # Global maximum
    best_root = -1   # Corresponding root index

    # Bottom-up DP
    for i in range(n - 1, -1, -1): # From last node to root node
        if not valid[i]: # Non-real node, value is 0
            dp[i] = 0
            continue
        # Calculate left and right subtree contributions
        left = 2 * i + 1
        right = 2 * i + 2

        left_dp = dp[left] if left < n and valid[left] else 0
        right_dp = dp[right] if right < n and valid[right] else 0

        # Allow pruning subtrees with non-positive contribution
        cur = arr[i]
        if left_dp > 0:
            cur += left_dp
        if right_dp > 0:
            cur += right_dp

        dp[i] = cur

        # Update global maximum and corresponding root node
        if best_sum is None or cur > best_sum:
            best_sum = cur
            best_root = i

    # Represents only None nodes
    if best_root == -1: 
        return []

    # BFS construct the pruned max subtree (complete binary tree form), best_root corresponds to subtree root index in original array
    # Calculate subtree node count
    
    res = []
    q = deque()
    # Queue element: (original array index, new tree index)
    q.append((best_root, 0))

    while q:
        oi, ni = q.popleft() # original index, new index

        # Inserted are all valid nodes, valid nodes are preceded by None
        while len(res) <= ni:
            res.append(None)
        
        # Insert current node value
        res[ni] = arr[oi]
        # Left child node
        left = 2 * oi + 1
        # Right child node
        right = 2 * oi + 2
        # Enqueue left child node
        if left < n and valid[left] and dp[left] > 0: # Only enqueue subtrees with contribution > 0
            q.append((left, 2 * ni + 1))
        # Enqueue right child node
        if right < n and valid[right] and dp[right] > 0:
            q.append((right, 2 * ni + 2))

    # # Remove trailing extra None -> Should not have None nodes at the very end
    # while res and res[-1] is None:
    #     res.pop()

    return res


def main():
    s = sys.stdin.readline().strip()
    if not s:
        return
    s = s.replace('null', 'None')
    arr = literal_eval(s)  # Get list containing int and None

    ans = max_pruned_subtree(arr)

    # Output format: [1,-1,null,2,...]
    out = '[' + ','.join('null' if x is None else str(x) for x in ans) + ']'
    print(out)


if __name__ == "__main__":
    main()
