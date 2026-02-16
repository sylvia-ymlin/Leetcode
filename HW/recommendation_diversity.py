# Distribute elements of M lists evenly into N windows
# Each window needs K elements, from different lists
# Need to distribute elements of each list as evenly as possible into N parts

# Just simulate

n = int(input())
k = int(input())
elems= []
while True:
    try:
        lst = list(map(int, input().split()))
        elems.append(lst)
    except EOFError:
        break

output_length = [0 for k in range(len(elems))] # Record count of output elements for each list
res = []

# Take numbers from lists in turn
# Take numbers first, calculate correct index when outputting
# For current list, if enough length, take n elements
# If not enough, take as many as possible
# When outputting, skip by n
while True:
    if len(res) >= n * k: # Taken enough for N windows, K elements each
        break
    else:
        # Take from each list
        for i in range(len(elems)):
            used = output_length[i]
            new_used = min(used + n, len(elems[i]))
            res += elems[i][used:new_used]
            output_length[i] = new_used

output = ""
for i in range(n):
    for j in range(k):
        idx = i + j * n
        output += str(res[idx]) + " "

print(output.strip())