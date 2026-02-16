"""
2025-10-33, L1
A set of engines, circular, manually start some, number and IDs of engines started at the last moment
Simulation, basic idea is Breadth First Search (BFS), use queue to record engines that will automatically start
"""

import sys
from collections import deque

def main():
    # Read all input
    # Read first line, number of engines and number of start info
    N, E = map(int, sys.stdin.readline().strip().split())
    # Hash map to store engine IDs started at each moment
    engine_starts = {}
    min_time = float('inf') # Record earliest start time
    # Iterate through each start info
    for _ in range(E):
        T, p = map(int, sys.stdin.readline().strip().split())
        if T not in engine_starts: # No start record yet
            engine_starts[T] = []
        engine_starts[T].append(p) # Record engine ID started at this moment
        min_time = min(min_time, T)
    
    queue = deque() # Queue for simulating engine starts
    # Record started engines
    checked = [False] * N
    # Record number of started engines
    cnt = 0
    cur_time = min_time

    while cnt < N:
        # Queue records engines that will automatically start in this layer
        res = []
        n = len(queue)
        for _ in range(n):
            engine = queue.popleft() # Dequeue
            if checked[engine]:
                continue
            checked[engine] = True
            cnt += 1
            res.append(engine)  # Record started engine ID
            # Enqueue neighboring engines
            queue.append((engine - 1 + N) % N) # Left neighbor
            queue.append((engine + 1) % N)     # Right neighbor
    
        # Manual start
        if cur_time in engine_starts:
            for engine in engine_starts[cur_time]:
                if not checked[engine]:
                    # Start
                    checked[engine] = True
                    cnt += 1
                    res.append(engine)
                    # Enqueue neighboring engines
                    queue.append((engine - 1 + N) % N) # Left neighbor
                    queue.append((engine + 1) % N)     # Right neighbor
        # Time advances
        cur_time += 1

    print(len(res))
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()
