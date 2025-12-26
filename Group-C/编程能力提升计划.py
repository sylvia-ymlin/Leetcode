# 有一组题，小王最多花 m 天完成
# 第一组数给出每道题目需要花费的时间
# 每天可以有一道题查看答案，不花费时间
# 求小王话费时间最多的一天花费了多少时间

# 题目限制，必须按照顺序刷题

# 要最小化每天花费时间的最大值，二分查找，找到这个 T
# T 是每天花费时间的最大值, 且 T 一定在 [0, sum(times)] 之间
# 拿到 T 后，贪心地分配每天的任务，判断是否能在 m 天内完成

def check(times, m, T):
    used_days = 1 # 至少一天
    sum_time = 0
    max_time = times[0]
    for t in times:
        sum_time += t
        max_time = max(max_time, t)
        # 减去当前最大时间题目，还是不能完成
        if sum_time - max_time > T: 
            # 必须要到下一天
            used_days += 1
            sum_time = t
            max_time = t
            if used_days > m:
                return False
    return True


def minTime(times, m):
    l, r = 0, sum(times)
    while l < r:
        mid = (l + r) >> 1
        if check(times, m, mid): # 如果 mid 可行，则尝试更小的值
            r = mid
        else: # 如果 mid 不可行，则尝试更大的值
            l = mid + 1
    # 一定会有解
    return l

times = list(map(int, input().split(',')))
m = int(input())

print(minTime(times, m))
