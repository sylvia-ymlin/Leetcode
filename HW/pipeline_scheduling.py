# Factory has m pipelines, completing n independent jobs in parallel
# Scheduling system always prioritizes jobs with shorter operation time
# Guaranteed valid input
# Output time required to complete all jobs

m, n = map(int, input().split())
times = list(map(int, input().split()))

# Sort by time, always shortest job first?
# "Prioritize jobs with shorter operation time".
# This sounds like Shortest Job First (SJF) scheduling which minimizes average waiting time,
# but here we want "time required to complete all jobs" (makespan).
# To minimize makespan on parallel machines is NP-hard (partition problem).
# But problem says "always prioritizes processing shorter jobs".
# This implies a specific strategy: Sort jobs by time, then assign.
# Just simulate: assign next job to the pipeline that finishes earliest (greedy).
# The code implements: Sort times.
# Then lines = [0]*m.
# Loop times: lines[i % m] += times[i].
# This is Round Robin assignment after sorting?
# No, `i % m` means assigning purely based on index.
# This assumes pipelines are available in round-robin fashion or something?
# Or maybe standard "Least Loaded" greedy?
# Assigning to `lines[i % m]` is NOT "earliest available" unless jobs are perfectly balanced.
# Actually, if we sort and assign round robin, it's a known heuristic.
# Let's assume the provided solution matches the problem's "scheduling system" logic, even if simple.
# Wait, "Always prioritize shorter jobs" refers to *job order*.
# The assignment logic `lines[i % m]` implies assignment strategy is fixed.
# I will just translate the code.

lines = [0] * m
times.sort()
for i in range(n):
    idx = i % m
    lines[idx] += times[i]

print(max(lines))