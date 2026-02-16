from queue import PriorityQueue
import sys

class Task:
    def __init__(self, id, priority, exec_time, arrival_time):
        self.id = id
        self.priority = priority
        self.remaining_time = exec_time
        self.arrival_time = arrival_time
        self.start_time = arrival_time

    def __lt__(self, other):
        # Priority queue comparison: higher priority first (value larger?), wait, code says:
        # if self.priority == other.priority: return self.arrival_time < other.arrival_time
        # return self.priority > other.priority.
        # This means larger priority value comes first?
        # Standard python PriorityQueue is min-heap.
        # If we want max-priority first, we should use negative priority or reverse logic.
        # Here `self.priority > other.priority` returning True means self is "smaller" in heap terms?
        # No, `__lt__` returning True means self comes before other in queue.
        # So `self.priority > other.priority` means higher value priority comes first.
        if self.priority == other.priority:
            return self.arrival_time < other.arrival_time
        return self.priority > other.priority


all_inputs = sys.stdin.read().strip().splitlines()
tasks = []
for line in all_inputs:
    id, priority, exec_time, arrival_time = map(int, line.split())
    tasks.append(Task(id, priority, exec_time, arrival_time))


wait_queue = PriorityQueue()
cpu_task = None
i = 0
n = len(tasks)
# Need to sort tasks by arrival time first?
# The code loop `while i < n` implies tasks are processed in order.
# Assuming input is sorted by arrival time? Or `i` index implies input order.
# The code doesn't sort `tasks`.
# If input is not sorted by arrival, logic `next_task = tasks[i]` is wrong.
# Let's assume input is sorted by arrival time or we should sort it.
# Standard scheduling problems usually give sorted input or we sort.
# The code doesn't sort, so assuming input is sorted.

# Loop runs until all tasks arrived and processed
current_time = 0 # Initialize current_time? code doesn't init it effectively before usage in some branches if cpu_task is None.
# Actually `cpu_task = None` branch:
# If queue empty: `cpu_task = next_task`, `current_time = cpu_task.arrival_time`. Correct.

while i < n or cpu_task or not wait_queue.empty():

    next_task = tasks[i] if i < n else None

    # CPU idle
    if cpu_task is None:
        # Take from wait queue
        if not wait_queue.empty():
            cpu_task = wait_queue.get()
            # Start time is max(arrival, current). 
            # If we just finished a task at current_time, we start immediately.
            # `cpu_task.start_time` is just a field, maybe updated?
            # Code: `cpu_task.start_time = current_time`
            # This looks like start of execution for this slice.
            cpu_task.start_time = current_time
        else: # Wait queue empty, take next arriving task
            cpu_task = next_task
            current_time = cpu_task.arrival_time
            cpu_task.start_time = current_time
            i += 1
        continue
    
    # Expected finish time of current task
    finish_time = cpu_task.start_time + cpu_task.remaining_time

    # If no next task, or next task arrives after current finishes
    if not next_task or finish_time <= next_task.arrival_time:
        current_time = finish_time
        print(f"{cpu_task.id} {current_time}")
        cpu_task = None
        continue

    # next task arrives before current finishes
    if next_task.priority > cpu_task.priority: # Preempt
        time_executed = next_task.arrival_time - cpu_task.start_time
        cpu_task.remaining_time -= time_executed
        wait_queue.put(cpu_task)

        current_time = next_task.arrival_time
        next_task.start_time = current_time
        cpu_task = next_task
    else: # Do not preempt, add next to wait queue
        wait_queue.put(next_task)

    i += 1