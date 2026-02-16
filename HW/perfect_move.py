# String of length multiple of 4, containing only characters W, A, S, D

# Read string
s = input().strip()
n = len(s)
# Count occurrences of each character
# Target count
target = n // 4
count = {'W':-target, 'A':-target, 'S':-target, 'D':-target}
for c in s:
    count[c.upper()] += 1

extra_chars = {c:cnt for c, cnt in count.items() if cnt > 0}

if not extra_chars:
    print(0)
    exit()

def can_shrink():
    for c, cnt in extra_chars.items():
        if mem[c] < cnt:
            return False
    return True

# Use sliding window to find shortest substring, count excess characters in window exactly == extra_chars
left = right = 0
res = n # Shortest substring length, limit n
mem = {c:0 for c in extra_chars}
while right < n:
    char_r = s[right].upper()
    if char_r in extra_chars:
        mem[char_r] += 1
    while can_shrink() and left <= right:
        res = min(res, right - left + 1)
        char_l = s[left].upper()
        if char_l in extra_chars:
            mem[char_l] -= 1
        left += 1
    # When exiting loop, substring pointed by left no longer satisfies condition, continue expanding right boundary
    right += 1

print(res)