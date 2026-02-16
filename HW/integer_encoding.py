# Encode input number in groups of 7 bits, highest bit indicates if there is more data
# Output encoded hexadecimal string

# Input a string representing non-negative integer
num_str = input().strip()
num = int(num_str)
# Convert to binary string
bin_str = bin(num)[2:] # Remove '0b' prefix
# Group by 7 bits, starting from low bits
res = ""
index = len(bin_str)
# Little-endian encoding, so first output is lowest bits
while len(bin_str) > 7:
    group = bin_str[-7:] # Take last 7 bits
    bin_str = bin_str[:-7] # Remove last 7 bits
    group = '1' + group # Highest bit set to 1, indicating more data
    res += group

# Remaining part
group = bin_str.zfill(8) # Pad with 0s to 8 bits, including highest bit 0 (implicit because loop condition >7 failed means remaining <=7 and we pad to 8, wait logic: if remaining is e.g. 101, zfill(8) becomes 00000101. Is the highest bit 0? Yes.)
res += group
# Binary string to hex, uppercase letters
hex_res = ""
for i in range(0, len(res), 8): # Convert 8 bits to 2 hex digits
    byte = res[i:i+8]
    # Binary to decimal then hex hex(int(byte, 2))
    # Remove '0x' [2:], pad 2 digits zfill(2), upper case .upper()
    hex_byte = hex(int(byte, 2))[2:].zfill(2).upper()
    hex_res += hex_byte

print(hex_res)
