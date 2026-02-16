# Query data within range, if not exists, ignore
# Compressed logs must be sorted in ascending order
# Time span less than 100, only need to check last 3 digits

start, end = input().replace(',', ' ').split()
n = int(input())
logs = []
for _ in range(n):
    log_start, log_end, data = input().replace(',', ' ').split()
    logs.append((log_start, log_end, data))

current = int(start[-3:])
idx = 0
while current <= int(end[-3:]) and idx < n:
    log_start, log_end, data = logs[idx]
    if int(log_end[-3:]) < current:
        idx += 1
        continue # Not in log range, skip, check next log
    if int(log_start[-3:]) > int(end[-3:]):
        break # Exceed query range, end
    # Output query for current moment
    print(f"{start[:-3]}{str(current).zfill(3)},{data}")
    current += 1
