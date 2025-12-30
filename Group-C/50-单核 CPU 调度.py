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

# 所有任务都到达，且等待队列和 CPU 空闲时结束
while i < n or cpu_task or not wait_queue.empty():

    next_task = tasks[i] if i < n else None

    # CPU 空闲时
    if cpu_task is None:
        # 从等待队列取任务
        if not wait_queue.empty():
            cpu_task = wait_queue.get()
            cpu_task.start_time = current_time
        else: # 等待队列空，取下一个到达的任务
            cpu_task = next_task
            current_time = cpu_task.arrival_time
            cpu_task.start_time = current_time
            i += 1
        continue
    
    # CPU 正在执行任务结束时间
    finish_time = cpu_task.start_time + cpu_task.remaining_time

    # 没有下一个任务，或下一个任务到达时间在当前任务结束之后，则执行当前任务至结束
    if not next_task or finish_time <= next_task.arrival_time:
        current_time = finish_time
        print(cpu_task.id, current_time)
        cpu_task = None
        continue

    # next task arrives before current finishes
    if next_task.priority > cpu_task.priority: # 抢占
        time_executed = next_task.arrival_time - cpu_task.start_time
        cpu_task.remaining_time -= time_executed
        wait_queue.put(cpu_task)

        current_time = next_task.arrival_time
        next_task.start_time = current_time
        cpu_task = next_task
    else: # 不抢占，加入等待队列
        wait_queue.put(next_task)

    i += 1