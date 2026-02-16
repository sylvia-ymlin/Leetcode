# Given a string with shuffled characters, restore original positive integer sequence

# Input
# Shuffled string, length of continuous positive integer sequence
# String length <= 200
# Positive integers <= 1000

s, n = input().split()
n = int(n)

# Determine digits of numbers in continuous sequence
# 1 digit: len(s) / n = 1
# 2 digits: len(s) / n = 2
# 3 digits: len(s) / n = 3
# 4 digits only one (1000)
# So if 1 < len(s) / n < 2 -> Mixed 1 and 2 digits
# If 2 < len(s) / n < 3 -> Mixed 2 and 3
# If 3 < len(s) / n -> Must contain 1000

# Sliding window, count occurrences of digits in continuous sequence. Since 1-2 digits very few, brute force enumerate all possible continuous sequences
from collections import Counter
nums = Counter(s)

left = 1
right = 1
current_count = {'0': 0, '1':0, '2': 0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}  # Digit -> Count
diff = 0
for i in range(10):
    if current_count[str(i)] != nums.get(str(i), 0):
        diff += 1

while right <= 1000:
    str_right = str(right)
    for ch in str_right:
        current_count[ch] += 1
        if current_count[ch] == nums.get(ch, 0):
            diff -= 1
        if current_count[ch] - 1 == nums.get(ch, 0):
            diff += 1
            # current_count exceeded nums, shrink window from left
            while left <= right and current_count[ch] > nums.get(ch, 0):
                str_left = str(left)
                for ch_left in str_left:
                    current_count[ch_left] -= 1
                    if current_count[ch_left] == nums.get(ch_left, 0): # Exactly matches
                        diff -= 1
                    if current_count[ch_left] + 1 == nums.get(ch_left, 0): # Was matching, now mismatch
                        diff += 1
                left += 1
     # Just matching char counts is not enough, must also match sequence length, because multiple sequences might have same char counts
     # Especially for n=1, we need to output smallest integer
    if diff == 0 and right - left + 1 == n: 
        break   # Found satisfying sequence
    right += 1

# Return smallest integer in sequence
print(left)