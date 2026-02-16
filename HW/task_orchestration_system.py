# Two types of tasks: Task A and Task B
# Task execution cannot be interrupted, and tasks can be executed consecutively
# In each orchestration, schedule 'num' tasks. Output total execution time of all possible orchestration schemes

# Input: time_A, time_B, num in one line
# Guaranteed numA > num and numB > num (available tasks sufficient?)
# Output: [t1, t2, ...] -> Sorted by execution time

# Total time for executing x Task A and (num - x) Task B

time_A, time_B, num = map(int, input().split(','))
results = set() # Use set to avoid duplicates
for x in range(num + 1):
    total_time = x * time_A + (num - x) * time_B
    results.add(total_time)

list_results = list(results)
list_results.sort()
print("[" + ",".join(map(str, list_results)) + "]")