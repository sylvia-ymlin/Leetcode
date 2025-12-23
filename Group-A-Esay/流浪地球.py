"""
2025-10-33, L1
一组发动机，环形，手动启动一些，最后一刻启动的发动机数量和编号
模拟，基本思想是广度优先搜索，用队列记录会自动启动的发动机
"""

import sys
from collections import deque

def main():
    # 读取所有输入
    # 读取第一行，发动机数量和启动信息数量
    N, E = map(int, sys.stdin.readline().strip().split())
    # 哈希表存储每个时刻启动的发动机编号
    engine_starts = {}
    min_time = float('inf') # 记录最早启动时间
    # 遍历每条启动信息
    for _ in range(E):
        T, p = map(int, sys.stdin.readline().strip().split())
        if T not in engine_starts: # 尚未有启动记录
            engine_starts[T] = []
        engine_starts[T].append(p) # 记录该时刻启动的发动机编号
        min_time = min(min_time, T)
    
    queue = deque() # 用于模拟发动机启动的队列
    # 记录已经启动的发动机
    checked = [False] * N
    # 记录启动的数量
    cnt = 0
    cur_time = min_time

    while cnt < N:
        # queue 中记录着本层会自动启动的发动机
        res = []
        n = len(queue)
        for _ in range(n):
            engine = queue.popleft() # 出队列
            if checked[engine]:
                continue
            checked[engine] = True
            cnt += 1
            res.append(engine)  # 记录启动的发动机编号
            # 临近发动机入队
            queue.append((engine - 1 + N) % N) # 左邻居
            queue.append((engine + 1) % N)     # 右邻居
    
        # 手动启动
        if cur_time in engine_starts:
            for engine in engine_starts[cur_time]:
                if not checked[engine]:
                    # 启动
                    checked[engine] = True
                    cnt += 1
                    res.append(engine)
                    # 临近发动机入队
                    queue.append((engine - 1 + N) % N) # 左邻居
                    queue.append((engine + 1) % N)     # 右邻居
        # 时间前进
        cur_time += 1

    print(len(res))
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()


