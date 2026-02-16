# Monthly pass cars not counted
# Non-monthly: 1 yuan per half hour; Less than half hour is free? No "Less than 30 mins not charged" -> Not charged if < 30 mins?
# Problem says "Less than half hour not charged; exceeding half hour, fractional part < half hour charged as half hour".
# Actually line 26: if total_time < 30 return 0. Line 28: (total_time + 29) // 30.
# Example: 31 mins -> 60 // 30 = 2 units?
# (31+29)//30 = 60//30 = 2. Yes.
# 11:30 - 13:30 daily is free
# Exceeding 8 hours not charged (capped at 8 hours fee?)
# "Exceeding 8 hours not charged" -> Capped at 8*60 mins logic in line 25.

def time_to_minutes(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

def calculate_cost(enter, leave):
    enter = time_to_minutes(enter)
    leave = time_to_minutes(leave)
    
    # Calculate total parking time
    total_time = leave - enter
    # Deduct free period
    free_start = time_to_minutes('11:30')
    free_end = time_to_minutes('13:30')
    if leave <= free_start or enter >= free_end:
        pass  # Not in free period
    else:
        overlap_start = max(enter, free_start)
        overlap_end = min(leave, free_end)
        total_time -= (overlap_end - overlap_start)
    total_time = min(total_time, 8 * 60)  # Capped at 8 hours
    if total_time < 30:
        return 0
    return (total_time + 29) // 30  # Ceiling division, 1 yuan per half hour

# Number of monthly pass cars entering/leaving
n = int(input())
# Monthly pass plate numbers
monthly_cars = set(input().split())
# Car records: Time, Plate, Action
# Time format HH:MM
records = []

while True:
    line = input()
    if not line:
        break
    time, plate, action = line.split()
    records.append((time, plate, action))


# Use set to store cars entering
res = 0
cars_info = {}
for time, plate, action in records:
    if plate in monthly_cars:
        continue
    if action == 'enter':
        cars_info[plate] = time
    else:
        enter_time = cars_info[plate]
        res += calculate_cost(enter_time, time)

print(res)
