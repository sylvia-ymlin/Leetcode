# 一共只有 5 台打印机

# 输入：
# 第一行：事件发生个数 
# 之后每一行：
# 事件类型 IN , 则表示有打印机进入队列，附带数据，打印机编号，文件优先级
# 事件类型 OUT , 则表示有打印机离开队列，附带数据，打印机编号

# 输出：
# 打印机打印的文件的编号，按事件发生顺序输出
# 如果没有文件打印，则输出 NULL

# 因为一共只有五个打印机，所以可以给每个打印机单独维护一个优先队列

# 输入
n = int(input())
# 读入事件
events = [input().split() for _ in range(n)]

import heapq
# 初始化五个打印机的优先队列
printers = {i: [] for i in range(1, 6)}
# 维护一个全局文件编号
file_counter = 1
for event in events:
    if event[0] == "IN":
        printer_id = int(event[1])
        file_priority = int(event[2])
        # 使用负优先级，因为 heapq 是小顶堆
        # push 时存入负优先级 和文件编号
        heapq.heappush(printers[printer_id], (-file_priority, file_counter))
        file_counter += 1
    elif event[0] == "OUT":
        printer_id = int(event[1])
        if printers[printer_id]:
            # 弹出优先级最高的文件
            print(heapq.heappop(printers[printer_id])[1])
        else:
            print("NULL")

