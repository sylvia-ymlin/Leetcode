# Given a string, count number of substrings that contain exactly k letters AND contain at least one of {0123456789}
# String contains only lowercase letters and digits

def is_char(c):
    return 'a' <= c <= 'z'

s = input().strip()
k = int(input().strip())

n = len(s)
res = 0
left = 0
count = 0
prex = 0 # Points to the current valid farthest left boundary

nums = {} # Record digit frequencies, to check if contains *all* digits?
# Wait, code says `len(nums) == 10`.
# This implies substring must contain ALL digits 0-9?
# Problem description in comment says "{0123456789} at least appear once".
# This usually means "Any digit appears" OR "All digits appear each at least once"?
# "Contain {0123456789} at least once" -> Likely means set of digits must include 0-9.
# The code `len(nums) == 10` confirms it requires ALL 10 digits to be present.

for right in range(n): # Right boundary extends gradually
    char_r = s[right]

    if is_char(char_r):
        count += 1
    else:
        nums[char_r] = nums.get(char_r, 0) + 1

    if count > k: # Letter count exceeded, move left boundary
        while left <= right and count > k:
            if not is_char(s[left]):
                nums[s[left]] -= 1
                if nums[s[left]] == 0:
                    del nums[s[left]]
            else:
                count -= 1
            left += 1
        prex = left
    
    if count == k and len(nums) == 10:
        # break -> Move left boundary, but ensure interval valid
        # We want to enable `prex` to move forward to count valid substrings ending at `right`.
        # `left` is the *start* of the minimal valid window ending at `right`.
        # As long as window `[left, right]` is valid (count==k, all digits), we can shrink from left
        # BUT we need to count how many valid start positions exist?
        # Actually `res += (left - prex + 1)`.
        # `prex` is the "hard" left bound (reset when count > k).
        # `left` is the "soft" left bound (moves forward as long as conditions Met? No, code logic is complex).
        # Let's see: `while left <= right and count == k and len(nums) == 10`.
        # Inside: check `s[left]`. Only if it is digit and we have spare (nums > 1), we remove it and `left++`.
        # If `s[left]` is letter, we break (because removing it would make count < k).
        # If `s[left]` is digit but count == 1, break (removing makes valid condition fail).
        # So `left` moves to the rightmost possible start of valid interval?
        # No, `left` moves to make window *minimal*?
        # Actually `left` moves to right as much as possible while maintaining validity.
        # So valid start indices are `prex` to `left`.
        # Check: `res += (left - prex + 1)`. Yes.
        # So `left` becomes the tightest left bound.
        while left <= right and count == k and len(nums) == 10:
            if not is_char(s[left]):
                if nums[s[left]] == 1:
                    break   
                else:
                    nums[s[left]] -= 1
                    left += 1
            else:
                break
        # Only count if left, prex, right are valid state
        # Actually logic is: valid starts are range [prex, left].
        res += (left - prex + 1)

print(res)
