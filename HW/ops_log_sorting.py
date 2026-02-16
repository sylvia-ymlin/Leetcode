# First line gives number of logs
# Then gives time of each log
# Sort chronologically, keep original format
# Format: H:M:S.N

import sys

n = int(input().strip())
times = []
for _ in range(n):
    times.append(input().strip())

# If format is completed, can sort strings directly
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