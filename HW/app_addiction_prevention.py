# 24 hours a day
# Register time slots available for each app. A time slot can only be occupied by one app
# For conflicting time slots, only one can be kept. Higher priority app is kept. If priority is same, keep the one registered earlier
# Input a time point, return the app that can be used at that time. If none, return NA

n = int(input().strip()) # App count
time_slots = [] # Store time slot and corresponding app name
for i in range(n):
    app_info = input().split()
    app_name = app_info[0]
    app_priority = int(app_info[1])
    start_time = app_info[2]
    end_time = app_info[3]
    # Time format fixed, lexicographical sort works
    if start_time < end_time:
        time_slots.append((start_time, end_time, app_name, app_priority))

# Read query time point
query_time = input().strip()

# Find app covering target time point
res = None
for slot in time_slots:
    start_time, end_time, app_name, app_priority = slot
    
    if not res:
        res = [start_time, end_time, app_name, app_priority]
        continue

    # Check priority
    existing_start, existing_end, existing_app, existing_priority = res
    if app_priority <= existing_priority:
        continue # Priority low or same, skip

    # Check conflict. Conflict: includes query time, replace; doesn't include, set empty
    if not(end_time < existing_start or start_time > existing_end):
        if start_time <= query_time < end_time: # Include start, exclude end
            res = [start_time, end_time, app_name, app_priority]
        else:
            res = None
        
print(res[2] if res else "NA")