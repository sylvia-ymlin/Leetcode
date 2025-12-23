# 第一行给出日志的条数
# 然后给出每个日志的时间
# 按时间先后顺序排序，保持原格式输出
# 格式为 H:M:S.N

import sys

n = int(input().strip())
times = []
for _ in range(n):
    times.append(input().strip())

# 如果补全格式，可以直接按字符串排序
formatted_times = []
for index, time in enumerate(times):
    H, M, S_N = time.split(':')
    S, N = S_N.split('.')
    H = H.zfill(2)
    M = M.zfill(2)
    S = S.zfill(2)
    N = N.zfill(3)
    # append including index
    formatted_times.append([f"{H}:{M}:{S}.{N}", index])

formatted_times.sort()

for ft, idx in formatted_times:
    print(times[idx])
    