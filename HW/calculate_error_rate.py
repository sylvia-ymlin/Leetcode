# Bit Error Rate (BER): In how many bits of data a single error occurs
# BER = Number of error bits / Total transmission bits
# Correctly transmitted characters and erroneously transmitted compressed storage
# Calculate BER

# Test cases guarantee decompressed lengths are consistent, i.e., only need to compare elements at same positions, no need to consider insertion or deletion

s1 = input().strip()  # Before transmission
s2 = input().strip()  # After transmission

# Parse compressed string: format is number + character
def parse_compressed_string(s: str) -> list:
    bits = []
    i = 0
    n = len(s)
    while i < n:
        # Read number first
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        # Read character
        char = s[i] if i < n else ''
        i += 1
        bits.append((char, num))  # Store as (character, count)
    return bits

s1_bits = parse_compressed_string(s1)
s2_bits = parse_compressed_string(s2)
total_bits = sum(count for _, count in s1_bits)  # Total bits

# Two pointers comparison
idx1 = 0  # Index for s1_bits
idx2 = 0  # Index for s2_bits
remain1 = s1_bits[0][1]  # Remaining count for current character
remain2 = s2_bits[0][1]  # If none, move to next character
error_bits = 0

# Decompressed lengths are equal, so actually won't have one side ending first
while idx1 < len(s1_bits) and idx2 < len(s2_bits):
    char1 = s1_bits[idx1][0] # Current s1 character
    char2 = s2_bits[idx2][0] # Current s2 character
    
    # Compare bits is minimum of remaining counts
    compare_bits = min(remain1, remain2)

    # Characters either equal or not
    # If different, all these bits are errors
    if char1 != char2:
        error_bits += compare_bits
    # If equal, update remaining bits directly
    # Update remaining bits
    remain1 -= compare_bits
    remain2 -= compare_bits
    
    # If a character is used up, move to next
    if remain1 == 0:
        idx1 += 1
        if idx1 < len(s1_bits): remain1 = s1_bits[idx1][1] 
    
    if remain2 == 0:
        idx2 += 1
        if idx2 < len(s2_bits): remain2 = s2_bits[idx2][1]

# Calculate BER and keep two decimal places
error_rate = error_bits / total_bits
print(f"{error_bits}" + '/' + f"{total_bits}")
