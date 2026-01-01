# 两种任务，Task A 和 task b
# 任务开始不能被打断，且任务可以连续执行
# 每次编排 num 个任务，输出任务所有可能的编排方案的总执行市场

# 第一行三个数： time_A， time_B， num
# 保证 numA > num, and numB > num
# 输出：[, , ,] -》 按执行时长从小到大排序

# 执行 x 个 task a， 和 num - x 个 task b 的总时长

time_A, time_B, num = map(int, input().split(','))
# results = []
results = set() # 用 set 避免重复
for x in range(num + 1):
    total_time = x * time_A + (num - x) * time_B
    # results.append(total_time)
    results.add(total_time)

# results.sort()
list_results = list(results)
list_results.sort()
print("[" + ",".join(map(str, list_results)) + "]")