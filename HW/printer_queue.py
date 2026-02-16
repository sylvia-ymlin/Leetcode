# There are only 5 printers

# Input:
# First line: Number of events
# Subsequent lines:
# Event type IN: Printer enters queue, with data: Printer ID, File Priority
# Event type OUT: Printer leaves queue (prints), with data: Printer ID

# Output:
# File ID of printed file, in order of events
# If no file to print, output NULL

# Since only 5 printers, maintain a priority queue for each

# Input
n = int(input())
# Read events
events = [input().split() for _ in range(n)]

import heapq
# Initialize priority queues for 5 printers
printers = {i: [] for i in range(1, 6)}
# Maintain global file ID
file_counter = 1
for event in events:
    if event[0] == "IN":
        printer_id = int(event[1])
        file_priority = int(event[2])
        # Use negative priority because heapq is min-heap
        # Store negative priority and file ID
        heapq.heappush(printers[printer_id], (-file_priority, file_counter))
        file_counter += 1
    elif event[0] == "OUT":
        printer_id = int(event[1])
        if printers[printer_id]:
            # Pop file with highest priority
            print(heapq.heappop(printers[printer_id])[1])
        else:
            print("NULL")
