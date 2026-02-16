# Given a matrix and an integer array
# Find minimal submatrix in the matrix that contains all data in the array
# Output minimal width of such submatrix

# Idea: Iterate matrix by columns, left, right maintain a sliding window
# Use a dictionary to record array elements and their counts in current window
# When window contains all array elements, try to shrink left boundary, update min width

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
