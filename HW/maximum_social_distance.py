# A row of N seats
# A group of employees enter and leave
# Guaranteed that leaving seat has an employee
# Entering employee keeps maximum social distance from others
# Prioritize sitting in smallest index seat

n = int(input())
# Read a list in format [1, 1, 1, 1, -4, 1]
ops = eval(input().strip())

# Seat indices 0 ~ n-1
# Use a set to record occupied seats
occupied = set()
# Output is the last person's seat position
res = -1
for op in ops:
    if op > 0:
        if len(occupied) == n:
            # Seats full, cannot sit
            print(res)
            exit(0)
        # Find seat position
        if len(occupied) == 0:
            res = 0
        else:
            seats = sorted(occupied)
            best_dist = -1
            best_pos = -1
            prev = -1
            max_gap = [0, -1, n] # Record max gap, left bound, right bound
            for cur in seats:
                if prev == -1:
                    dist = cur
                    pos = 0
                else:
                    dist = (cur - prev) // 2
                    pos = prev + dist
                if dist > best_dist:
                    best_dist = dist
                    best_pos = pos
                prev = cur
            # Handle distance from last seat to n-1
            # Right end interval
            if n - 1 - prev > best_dist:
                best_pos = n - 1
            res = best_pos
        occupied.add(res)
    else:
        # Leave
        leave_pos = -op
        occupied.remove(leave_pos)
# Output final occupied position
print(res)
