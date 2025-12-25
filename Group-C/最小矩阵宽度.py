# 给定一个矩阵，和一个整数数组
# 在矩阵中找到包含数组中所有数据的最小子矩阵
# 输出该子矩阵的最小宽度

# 思路：按列遍历矩阵，left、right 维持一个滑动窗口
# 用一个字典记录当前窗口中包含的数组元素及其出现次数
# 当窗口包含所有数组元素时，尝试收缩左边界，更新最小宽度

from collections import Counter, defaultdict

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
arr = list(map(int, input().split()))
arr_cnt = Counter(arr)

min_width = float('inf')
left = right = 0
window_cnt = defaultdict(int)
for right in range(m):
    for row in range(n):
        val = matrix[row][right]
        if val in arr_cnt:
            window_cnt[val] += 1
    
    while all(window_cnt[x] >= arr_cnt[x] for x in arr_cnt):
        min_width = min(min_width, right - left + 1)
        for row in range(n):
            val = matrix[row][left]
            if val in arr_cnt:
                window_cnt[val] -= 1
        left += 1
        
if min_width == float('inf'):
    print(-1)
else:
    print(min_width)

    

