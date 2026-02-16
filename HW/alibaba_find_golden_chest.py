# Chests numbered 0-N, each chest has a number on it
# Given a number k, check if there exist two chests with the same number, and the difference between their indices is at most k
# If exists, return the smallest chest index among such pairs; otherwise return -1

# Read numbers on chests
nums = list(map(int, input().split(',')))
# Read k
k = int(input())

# Use sliding window, maintain a window of size at most k
# When such a pair is found, nums[left] == nums[right], return left

# Use set to check duplicate numbers. If exists, move left to find this number
seen = set()
left = right = 0
n = len(nums)
while right < n:
    if nums[right] in seen:
        while nums[left] != nums[right]:
            seen.remove(nums[left])
            left += 1
        
        if right - left <= k:
            print(left)
            exit(0)
    
    seen.add(nums[right])
    right += 1
print(-1)