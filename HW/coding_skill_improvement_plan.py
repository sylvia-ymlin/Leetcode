# A set of problems, Alice can spend at most m days to complete
# First line gives time required for each problem
# Can check answer for one problem per day, taking no time
# Find minimum max daily time spent

# Constraint: must solve problems in order

# Minimize the maximum daily time spent, binary search to find this T
# T is max daily time, and T must be between [0, sum(times)]
# With T, greedily assign daily tasks, check if can complete within m days

def check(times, m, T):
    used_days = 1 # At least one day
    sum_time = 0
    max_time = times[0]
    for t in times:
        sum_time += t
        max_time = max(max_time, t)
        # Minus current max time problem, still exceeds T
        if sum_time - max_time > T: 
            # Must maximize use of free pass for largest task of the day
            # If (sum - max) > T, means current task cannot fit even with help
            # So start new day with current task
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
        if check(times, m, mid): # If mid is feasible, try smaller
            r = mid
        else: # If mid not feasible, try larger
            l = mid + 1
    # Solution must exist
    return l

times = list(map(int, input().split(',')))
m = int(input())

print(minTime(times, m))
