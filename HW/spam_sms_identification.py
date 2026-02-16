# Identify spam SMS senders
# Condition (any one met means spammer):
# 1. Among recipients of A's SMS, number of people L who haven't sent SMS to A > 5
# 2. SMS sent by A - SMS received by A = M > 10
# 3. Exists X such that A sent to X - A received from X > 5

# Max ID 100
# Build 100x100 matrix, matrix[i][j] means count sent from i to j

MAX_ID = 100

matrix = [[0] * (MAX_ID + 1) for _ in range(MAX_ID + 1)]

# Read number of records
n = int(input().strip())
for _ in range(n):
    sender, receiver = map(int, input().strip().split())
    matrix[sender][receiver] += 1

# Target ID to judge
target_id = int(input().strip())

# Calculate L and M
L = 0 # Recipients who didn't reply to target_id
is_spam = False

for j in range(0, MAX_ID + 1):
    if matrix[target_id][j] > 0:
        if matrix[j][target_id] == 0:
            L += 1
        # Condition 3: A sent to X - X sent to A > 5
        if matrix[target_id][j] - matrix[j][target_id] > 5:
            is_spam = True

# Condition 2: Total Sent - Total Received > 10
sent_count = sum(matrix[target_id])
received_count = sum(matrix[i][target_id] for i in range(1, 101)) # range(101) covers 0-100
M = sent_count - received_count

res = 'true' if (L > 5 or M > 10 or is_spam) else 'false'
print(f"{res} {L} {M}")