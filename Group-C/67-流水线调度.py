# 工厂 m 条流水线，并行完成 n 个独立作业
# 建立一个调度系统，安排作业时，总是优先处理操作时间较短的作业
# 保证输入都是合法的
# 输出完成所有作业所需的时间

m, n = map(int, input().split())
times = list(map(int, input().split()))

# 按照时间排序，总是第一条流水线先完成
# 不断遍历流水线即可，记录每个流水线的操作时间

lines = [0] * m
times.sort()
for i in range(n):
    idx = i % m
    lines[idx] += times[i]

print(max(lines))