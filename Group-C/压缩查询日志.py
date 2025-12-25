# 查询范围内的数据，如果不存在，就忽略
# 压缩的日志一定按照升序排列
# 时间跨度小于 100，只需要看最后3位

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
        continue # 不在该日志范围内，跳过，继续找下一个日志
    if int(log_start[-3:]) > int(end[-3:]):
        break # 超出查询范围，结束
    # 输出当前时刻查询
    print(f"{start[:-3]}{str(current).zfill(3)},{data}")
    current += 1


# 202411231010,202411231013
# 4
# 202411231000,202411231010,11
# 202411231011,202411231012,10
# 202411231013,202411231020,16
# 202411231021,202411231028,17

