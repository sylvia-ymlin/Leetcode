# 编号 0-N 的箱子，每个箱子上有一个数字
# 给出一个数字 k，查看是否存在两个箱子上的数字相等，且两个箱子的编号之差不超过 k
# 存在，返回这对箱子中编号最小的箱子编号；不存在，返回 -1

# 读入箱子上的数字
nums = list(map(int, input().split(',')))
# 读入 k
k = int(input())

# 使用滑动窗口，维护一个大小不超过 k 的窗口
# 当找到这样的一对数字时， nums[left] == nums[right], 返回 left

# 使用 set 判断是否存在重复数字，存在时，移动 left 找到这个数字
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