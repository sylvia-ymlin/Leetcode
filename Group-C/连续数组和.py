# 求 和大于 x 的 连续子数组个数

# 连续子数组，且元素都是正数
# 前缀和，找到一个前缀和大于 x 的，则后续所有前缀和都大于 x

n, x = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

count = 0
right = 0
for left in range(n):
    # 找到以 left 开头和大于等于 x 的最小右端点
    while right < n and prefix_sum[right + 1] - prefix_sum[left] < x:
        right += 1
    # 以 [left, right] 开头的子数组个数
    count += n - right

print(count)
    