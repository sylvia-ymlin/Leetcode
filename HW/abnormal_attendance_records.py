# Abnormal Attendance:
# 1. Actual device ID is different from registered device ID
# 2. Same employee has two attendance records within 60 minutes, and distance is over 5km

# First line outputs number of attendance records
# Starting from second line, input attendance records: ID, time, attendance distance, actual device ID, registered device ID

# Output abnormal attendance records in input order, separated by “;”
# If none, output “null”

n = int(input())
records = [input().split(',') for _ in range(n)]
# Sort by ID and time
# Need to output abnormal records in input order, so add index
records = [(i, *records[i]) for i in range(n)] # Need to use * to unpack records[i]
records.sort(key=lambda x: (x[1], x[2]))

cur_id = records[0][1]
unusual_records = set()
i = 0
while i < len(records):
    # Check device ID
    if records[i][4] != records[i][5]:
        unusual_records.add(records[i])
    
    # Check if same person as previous record
    if i > 0 and records[i][1] == records[i-1][1]:
        # Calculate time and distance
        diff_time = int(records[i][2]) - int(records[i-1][2])
        diff_dist = abs(int(records[i][3]) - int(records[i-1][3]))
        # Check time and distance
        if diff_time < 60 and diff_dist > 5:
            if records[i-1] not in unusual_records: # Avoid duplicate addition
                unusual_records.add(records[i-1])
            unusual_records.add(records[i])
    i += 1 # Move to next record
    

# Sort by index to restore input order
unusual_records = list(unusual_records)
unusual_records.sort(key=lambda x: x[0])
# Remove index
unusual_records = [r[1:] for r in unusual_records]
# Output
print(";".join(",".join(r) for r in unusual_records) if unusual_records else "null")