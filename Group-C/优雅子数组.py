# 给出一个数组，找到 数组中的所有优雅子数组 。
# 优雅子数组：数组中出现次数最多元素大等于 k

# 存在型约束问题：要求出现次数 >= k

from collections import defaultdict

n, k = map(int, input().split())

nums = list(map(int, input().split()))

res = 0
cnt = defaultdict(int)
left = 0

for right in range(n):
    x = nums[right]
    cnt[x] += 1
    # 判断是否找到了元素出现次数为 k 的子数组
    if cnt[x] == k:
        # 则所有以 [left，right] 为前缀的子数组都是优雅子数组
        res += n - right  # 以 right 结尾的子数组有 n

        # 左边界移动
        while cnt[x] >= k:
            y = nums[left]
            cnt[y] -= 1
            left += 1
            if y != x: # 仍然是优雅子数组
                res += n - right

print(res) 