# Do not process content inside single quotes
# Otherwise, for consecutive spaces within given coordinate ranges, keep only one
# Output string after removing spaces, and modified coordinate ranges

s = input()
coords_str = input().split(',')
coords = [tuple(map(int, c.split())) for c in coords_str]

# Mark positions in given ranges
in_range = [False] * len(s)
for start, end in coords:
    for i in range(start, end + 1):
        in_range[i] = True

# Mark characters to keep
keep = [True] * len(s)
in_quote = False

i = 0
while i < len(s):
    if s[i] == "'":
        in_quote = not in_quote
        i += 1
        continue
    
    # In range AND not in quote AND is space
    if in_range[i] and not in_quote and s[i] == ' ':
        # Find start of consecutive spaces
        j = i
        while j < len(s) and s[j] == ' ' and in_range[j] and not in_quote:
            j += 1
        # Keep first space, delete rest
        for k in range(i + 1, j):
            keep[k] = False
        i = j
    else:
        i += 1

# Build new string
new_s = ''.join(s[i] for i in range(len(s)) if keep[i])

# Calculate deleted characters before each position (prefix sum)
deleted_before = [0] * (len(s) + 1)
for i in range(len(s)):
    deleted_before[i + 1] = deleted_before[i] + (0 if keep[i] else 1)

# Adjust coordinates
new_coords = []
for start, end in coords:
    new_start = start - deleted_before[start]
    new_end = end - deleted_before[end + 1]
    new_coords.append(f"{new_start} {new_end}")

print(new_s)
print(','.join(new_coords))
