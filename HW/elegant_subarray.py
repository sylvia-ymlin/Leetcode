# Given an array, find all elegant subarrays in it.
# Elegant subarray: The most frequent element in the array appears at least k times

# Existence constraint problem: requires occurrence count >= k

from collections import defaultdict

n, k = map(int, input().split())

nums = list(map(int, input().split()))

res = 0
cnt = defaultdict(int)
left = 0

for right in range(n):
    x = nums[right]
    cnt[x] += 1
    # Check if we found a subarray where element appears k times
    if cnt[x] == k:
        # Then all subarrays with prefix [left, right] are elegant subarrays
        res += n - right  # There are n-right subarrays ending at right? No, starting from left... logic is a bit weird.
                          # Actually, if [left, right] satisfies condition, then [left, right], [left, right+1]... [left, n-1] satisfy? No.
                          # Wait, code logic: if window [left, right] has element x appearing k times.
                          # Then any subarray starting at <=left and ending at >=right containing this window satisfies?
                          # The code adds `n - right`. This usually means for a fixed left, valid rights are from right to n-1. 
                          # But here `right` is fixed. `n - right` doesn't make sense if iterating right.
                          # Ah, explanation: for a FIXED right, we want to find how many lefts satisfy.
                          # Actually: if `cnt[x] == k`, it means we found a window [something...right] where x appears k times.
                          # The code logic seems to be: once condition met, shrink left.
        
        # Shrink left boundary
        while cnt[x] >= k:
            y = nums[left]
            cnt[y] -= 1
            left += 1
            if y != x: # Still an elegant subarray (because removing y didn't reduce count of x below k, or x was the one)
                       # Wait, we need to count subarrays.
                       # If [left...right] is valid, then [0...right], [1...right] are also valid?
                       # No, problem says "most frequent element >= k".
                       # If [left...right] has x count k, and we remove from left.
                       # This algorithm is counting subarrays.
                       # `res += n - right` logic is usually for "at least k" with fixed left?
            # Let's just translate the comments.
                res += n - right

print(res) 